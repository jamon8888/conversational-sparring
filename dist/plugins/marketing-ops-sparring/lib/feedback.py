"""Structured feedback generation for the Conversational Sparring.

Adapted from PMM's reflection_synthesizer.py with domain-aware feedback.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .domains import DomainConfig

try:
    from .ledger import SparringLedger
except ImportError:
    from ledger import SparringLedger

try:
    from .domains import load_domain, get_default_domain
except ImportError:
    # Fallback for standalone testing
    load_domain = None  # type: ignore
    get_default_domain = None  # type: ignore


class FeedbackSeverity(str, Enum):
    """Severity levels for feedback."""
    CELEBRATION = "celebration"  # Achievement recognition
    NUDGE = "nudge"              # Gentle reminder
    SUGGESTION = "suggestion"    # Actionable recommendation
    WARNING = "warning"          # Important issue to address


@dataclass
class FeedbackItem:
    """A single piece of feedback."""
    category: str
    message: str
    severity: FeedbackSeverity
    actionable: bool = True
    context: Optional[str] = None


class FeedbackGenerator:
    """Generate structured, personalized feedback from sparring data.

    Uses domain configuration for customized messages and thresholds.
    """

    def __init__(
        self,
        ledger: SparringLedger,
        domain: Optional["DomainConfig"] = None,
        domain_id: Optional[str] = None,
    ) -> None:
        """Initialize FeedbackGenerator.

        Args:
            ledger: Sparring ledger instance
            domain: Optional pre-loaded domain config
            domain_id: Optional domain ID to load (ignored if domain provided)
        """
        self.ledger = ledger

        # Load domain config
        if domain is not None:
            self._domain = domain
        elif domain_id is not None and load_domain is not None:
            self._domain = load_domain(domain_id)
        elif load_domain is not None and get_default_domain is not None:
            self._domain = load_domain(get_default_domain())
        else:
            # Fallback: no domain config
            self._domain = None

    @property
    def domain(self) -> Optional["DomainConfig"]:
        """Get current domain configuration."""
        return self._domain

    def _get_message(self, key: str, default: str) -> str:
        """Get message from domain config or use default."""
        if self._domain:
            return self._domain.get_message(key, default)
        return default

    def _get_threshold(self, key: str, default: Any) -> Any:
        """Get threshold from domain config or use default."""
        if self._domain:
            return self._domain.get_threshold(key, default)
        return default

    def generate_post_work_feedback(
        self,
        goal_id: Optional[str] = None,
        work_summary: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generate feedback after completing work.

        Format: Corrections -> Progress -> Observations -> Next

        Args:
            goal_id: Optional goal ID this work relates to
            work_summary: Optional summary of what was done

        Returns:
            Structured feedback dict
        """
        feedback: Dict[str, List[FeedbackItem]] = {
            "corrections": [],
            "progress": [],
            "observations": [],
            "next_steps": [],
        }

        # Analyze recent events
        recent_events = self.ledger.read_tail(50)

        # Check for corrections needed
        corrections = self._detect_corrections(recent_events)
        feedback["corrections"] = corrections

        # Track progress
        progress = self._assess_progress(recent_events, goal_id)
        feedback["progress"] = progress

        # Generate observations
        observations = self._generate_observations(recent_events)
        feedback["observations"] = observations

        # Suggest next steps
        next_steps = self._suggest_next_steps(recent_events, goal_id)
        feedback["next_steps"] = next_steps

        # Build summary
        summary = self._build_summary(feedback, work_summary)

        return {
            "summary": summary,
            "feedback": {
                k: [self._item_to_dict(item) for item in v]
                for k, v in feedback.items()
            },
            "has_critical": any(
                item.severity == FeedbackSeverity.WARNING
                for items in feedback.values()
                for item in items
            ),
        }

    def generate_reflection_prompt(
        self,
        recent_activity: Optional[str] = None,
    ) -> Dict[str, str]:
        """Generate a structured reflection prompt.

        Returns:
            Dict with prompts for intent, outcome, and next
        """
        return {
            "intent_prompt": "What were you trying to accomplish?",
            "outcome_prompt": "What actually happened?",
            "next_prompt": "What will you do next?",
            "context": recent_activity or "No recent activity recorded",
        }

    def record_reflection(
        self,
        intent: str,
        outcome: str,
        next_action: str,
        goal_id: Optional[str] = None,
    ) -> int:
        """Record a structured reflection in the ledger.

        Args:
            intent: What was the intent
            outcome: What happened
            next_action: What's next
            goal_id: Optional related goal

        Returns:
            Event ID
        """
        content = json.dumps({
            "intent": intent[:256],
            "outcome": outcome[:256],
            "next": next_action[:256],
        }, sort_keys=True)

        meta: Dict[str, Any] = {
            "synth": "sparring",
            "source": "user_reflection",
        }

        if goal_id:
            meta["goal_id"] = goal_id

        return self.ledger.append(
            kind="reflection",
            content=content,
            meta=meta,
        )

    def record_feedback(
        self,
        feedback_type: str,
        message: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> int:
        """Record feedback given to user in the ledger."""
        content = json.dumps({
            "type": feedback_type,
            "message": message,
            "context": context,
        }, sort_keys=True)

        meta = {
            "feedback_type": feedback_type,
        }

        return self.ledger.append(
            kind="feedback",
            content=content,
            meta=meta,
        )

    def _detect_corrections(
        self,
        events: List[Dict[str, Any]]
    ) -> List[FeedbackItem]:
        """Detect issues that need correction."""
        corrections = []

        # Check for struggles
        recent_struggles = [
            e for e in events if e.get("kind") == "struggle"
        ]
        if len(recent_struggles) >= 2:
            corrections.append(FeedbackItem(
                category="repeated_struggle",
                message="Multiple struggles detected - consider taking a different approach",
                severity=FeedbackSeverity.WARNING,
                actionable=True,
            ))

        # Check for abandoned goals
        recent_abandons = [
            e for e in events if e.get("kind") == "goal_abandon"
        ]
        if recent_abandons:
            abandon_msg = self._get_message(
                "goal_abandoned",
                "A goal was abandoned - reflect on what blocked completion"
            )
            corrections.append(FeedbackItem(
                category="goal_abandoned",
                message=abandon_msg,
                severity=FeedbackSeverity.SUGGESTION,
                actionable=True,
            ))

        return corrections

    def _assess_progress(
        self,
        events: List[Dict[str, Any]],
        goal_id: Optional[str],  # noqa: ARG002 - reserved for future use
    ) -> List[FeedbackItem]:
        """Assess progress made."""
        progress = []

        # Count completions
        closed_goals = [
            e for e in events if e.get("kind") == "goal_close"
        ]
        if closed_goals:
            complete_msg = self._get_message(
                "goal_completed",
                f"Completed {len(closed_goals)} goal(s) recently"
            )
            if "{count}" not in complete_msg:
                complete_msg = f"Completed {len(closed_goals)} goal(s) recently"

            progress.append(FeedbackItem(
                category="goals_completed",
                message=complete_msg,
                severity=FeedbackSeverity.CELEBRATION,
                actionable=False,
            ))

        # Check for achievements
        achievements = [
            e for e in events if e.get("kind") == "achievement"
        ]
        if achievements:
            latest = achievements[-1]
            content_str = latest.get("content", "{}")
            try:
                content = json.loads(content_str)
                ach_type = content.get("type", "achievement")
                streak = content.get("streak", 0)

                # Use domain message for streak if available
                if streak > 0:
                    streak_msg = self._get_message(
                        "streak_message",
                        f"{streak} in a row"
                    )
                    streak_msg = streak_msg.replace("{count}", str(streak))
                    progress.append(FeedbackItem(
                        category="streak",
                        message=streak_msg,
                        severity=FeedbackSeverity.CELEBRATION,
                        actionable=False,
                    ))
                else:
                    progress.append(FeedbackItem(
                        category="achievement",
                        message=f"Achievement unlocked: {ach_type}!",
                        severity=FeedbackSeverity.CELEBRATION,
                        actionable=False,
                    ))
            except json.JSONDecodeError:
                pass

        # Check reflections
        reflections = [
            e for e in events if e.get("kind") == "reflection"
        ]
        if reflections:
            progress.append(FeedbackItem(
                category="reflection_active",
                message="Good reflection habits - keep it up!",
                severity=FeedbackSeverity.NUDGE,
                actionable=False,
            ))

        return progress

    def _generate_observations(
        self,
        events: List[Dict[str, Any]]
    ) -> List[FeedbackItem]:
        """Generate observations about work patterns."""
        observations = []

        # Count event types
        kind_counts: Dict[str, int] = {}
        for e in events:
            kind = e.get("kind", "unknown")
            kind_counts[kind] = kind_counts.get(kind, 0) + 1

        # Get max open goals threshold from domain
        max_open = self._get_threshold("max_open_goals", 7)

        # Observation: lots of goals opening
        if kind_counts.get("goal_open", 0) > 5:
            open_count = kind_counts["goal_open"]
            close_count = kind_counts.get("goal_close", 0) + kind_counts.get("goal_abandon", 0)
            active_goals = open_count - close_count

            if active_goals > max_open:
                observations.append(FeedbackItem(
                    category="too_many_goals",
                    message=f"You have {active_goals} active goals (recommended max: {max_open})",
                    severity=FeedbackSeverity.WARNING,
                    actionable=True,
                    context="Consider focusing on completion before starting new goals",
                ))
            elif open_count > close_count + 2:
                observations.append(FeedbackItem(
                    category="many_open_goals",
                    message=f"You have many open goals ({open_count - close_count} more opens than closes)",
                    severity=FeedbackSeverity.NUDGE,
                    actionable=True,
                    context="Consider focusing on completion before starting new goals",
                ))

        # Observation: frequent interventions
        if kind_counts.get("intervention", 0) >= 3:
            observations.append(FeedbackItem(
                category="frequent_help",
                message="I've been helping frequently - let me know if you want to try independently",
                severity=FeedbackSeverity.NUDGE,
                actionable=False,
            ))

        return observations

    def _suggest_next_steps(
        self,
        events: List[Dict[str, Any]],
        goal_id: Optional[str],  # noqa: ARG002 - reserved for future use
    ) -> List[FeedbackItem]:
        """Suggest next steps based on current state."""
        next_steps = []

        # Find open goals
        open_goals = self._count_open_goals(events)
        max_open = self._get_threshold("max_open_goals", 7)

        if open_goals == 0:
            next_steps.append(FeedbackItem(
                category="no_goals",
                message=f"No open goals - use /sparring goal to set a new objective",
                severity=FeedbackSeverity.SUGGESTION,
                actionable=True,
            ))
        elif open_goals > max_open:
            next_steps.append(FeedbackItem(
                category="too_many_goals",
                message=f"Many open goals ({open_goals}) - focus on closing some before adding more",
                severity=FeedbackSeverity.WARNING,
                actionable=True,
            ))
        else:
            next_steps.append(FeedbackItem(
                category="continue_work",
                message=f"Continue working on your {open_goals} active goal(s)",
                severity=FeedbackSeverity.NUDGE,
                actionable=True,
            ))

        # Check if reflection is due
        reflections = [e for e in events if e.get("kind") == "reflection"]
        if len(events) > 20 and len(reflections) == 0:
            next_steps.append(FeedbackItem(
                category="reflection_due",
                message="Consider reflecting on recent work with /sparring reflect",
                severity=FeedbackSeverity.SUGGESTION,
                actionable=True,
            ))

        return next_steps

    def _count_open_goals(self, events: List[Dict[str, Any]]) -> int:
        """Count currently open goals from events."""
        open_ids = set()
        for e in events:
            kind = e.get("kind")
            goal_id = e.get("meta", {}).get("goal_id", "")
            if kind == "goal_open" and goal_id:
                open_ids.add(goal_id)
            elif kind in ("goal_close", "goal_abandon") and goal_id:
                open_ids.discard(goal_id)
        return len(open_ids)

    def _build_summary(
        self,
        feedback: Dict[str, List[FeedbackItem]],
        work_summary: Optional[str],
    ) -> str:
        """Build a human-readable summary."""
        parts = []

        if work_summary:
            parts.append(f"Work: {work_summary}")

        correction_count = len(feedback["corrections"])
        if correction_count:
            parts.append(f"Issues to address: {correction_count}")

        progress_count = len([
            p for p in feedback["progress"]
            if p.severity == FeedbackSeverity.CELEBRATION
        ])
        if progress_count:
            parts.append(f"Wins: {progress_count}")

        # Use domain welcome message if available
        if not parts and self._domain:
            return self._domain.get_message("welcome", "Keep up the good work!")

        return " | ".join(parts) if parts else "Keep up the good work!"

    @staticmethod
    def _item_to_dict(item: FeedbackItem) -> Dict[str, Any]:
        """Convert FeedbackItem to dict."""
        return {
            "category": item.category,
            "message": item.message,
            "severity": item.severity.value,
            "actionable": item.actionable,
            "context": item.context,
        }

