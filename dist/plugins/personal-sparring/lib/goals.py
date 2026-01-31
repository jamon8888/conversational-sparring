"""Goal management for the Conversational Sparring Partner.

Adapted from PMM's commitment_manager.py with domain-agnostic goal tracking.
Categories and keywords are loaded from domain configuration.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from enum import Enum
from hashlib import sha1
from typing import Any, Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .domains import DomainConfig
    from .mirror import SparringMirror

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


class GoalOutcome(str, Enum):
    """Possible outcomes when closing a goal."""
    SUCCESS = "success"
    PARTIAL = "partial"
    ABANDONED = "abandoned"


def _parse_timestamp(ts: str) -> datetime:
    """Parse ISO timestamp to datetime."""
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return datetime.now(timezone.utc)


def _days_since(ts: str) -> float:
    """Calculate days since a timestamp."""
    dt = _parse_timestamp(ts)
    now = datetime.now(timezone.utc)
    return (now - dt).total_seconds() / 86400


class GoalManager:
    """Manage goal lifecycle operations against the ledger.

    Uses domain configuration for categories, keywords, and thresholds.
    """

    def __init__(
        self,
        ledger: SparringLedger,
        domain: Optional["DomainConfig"] = None,
        domain_id: Optional[str] = None,
        mirror: Optional["SparringMirror"] = None,
    ) -> None:
        """Initialize GoalManager.

        Args:
            ledger: Sparring ledger instance
            domain: Optional pre-loaded domain config
            domain_id: Optional domain ID to load (ignored if domain provided)
            mirror: Optional Mirror for O(1) goal lookups (recommended)
        """
        self.ledger = ledger
        self._mirror = mirror

        # Load domain config
        if domain is not None:
            self._domain = domain
        elif domain_id is not None and load_domain is not None:
            self._domain = load_domain(domain_id)
        elif load_domain is not None and get_default_domain is not None:
            self._domain = load_domain(get_default_domain())
        else:
            # Fallback: no domain config (use legacy behavior)
            self._domain = None

    @property
    def domain(self) -> Optional["DomainConfig"]:
        """Get current domain configuration."""
        return self._domain

    def open_goal(
        self,
        description: str,
        category: Optional[str] = None,
        deadline: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> str:
        """Open a new goal.

        Args:
            description: Goal description
            category: Category (auto-detected if not provided)
            deadline: Optional deadline (ISO format or natural language)
            tags: Optional list of tags

        Returns:
            Goal ID (first 8 chars of SHA1 hash)
        """
        description = (description or "").strip()
        if not description:
            raise ValueError("Goal description cannot be empty")

        # Create session_start event if this is the first goal in a new session
        # Check last 50 events for a recent session_start
        recent_events = self.ledger.read_tail(limit=50)
        has_recent_session = False

        if recent_events:
            from datetime import datetime, timezone, timedelta

            # Check if any session_start in last hour
            cutoff_time = datetime.now(timezone.utc) - timedelta(hours=1)
            for event in reversed(recent_events):  # Most recent first
                if event["kind"] == "session_start":
                    event_time = datetime.fromisoformat(event["ts"].replace("Z", "+00:00"))
                    if event_time > cutoff_time:
                        has_recent_session = True
                    break

        if not has_recent_session:
            from datetime import datetime, timezone

            session_meta = {
                "trigger": "goal_creation",
            }

            # Include domain if available
            if self._domain:
                session_meta["domain"] = self._domain.id

            self.ledger.append(
                kind="session_start",
                content=json.dumps({
                    "domain": self._domain.id if self._domain else "personal",
                    "trigger": "goal_creation",
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }, sort_keys=True),
                meta=session_meta,
            )

        # Detect cognitive mode (LEARNING vs DECISION)
        try:
            from .cognition import CognitiveRouter

            router = CognitiveRouter(self.ledger)
            mode, confidence = router.determine_mode(description)
            ere_level = router.get_current_ere_level()

            # Persist cognitive mode to ledger
            self.ledger.append(
                kind="cognitive_mode_switch",
                content=json.dumps({
                    "mode": mode.value,
                    "confidence": confidence,
                    "ere_level": ere_level.value,
                    "context": description[:100],
                }, sort_keys=True),
                meta={
                    "mode": mode.value,
                    "confidence": confidence,
                    "ere_level": ere_level.value,
                    "ere_name": ere_level.name,
                },
            )
        except ImportError:
            # Cognition module not available, skip
            pass

        # Detect category from description if not provided
        if not category:
            category = self._detect_category(description)
        else:
            # Validate category against domain config
            category = self._validate_category(category.lower())

        # Generate goal ID from description
        goal_id = sha1(description.encode("utf-8")).hexdigest()[:8]

        # Check for duplicate open goals
        if self._is_goal_open(goal_id):
            return goal_id  # Idempotent - return existing ID

        # Compute impact score based on description
        impact_score = self._compute_impact_score(description)

        meta: Dict[str, Any] = {
            "goal_id": goal_id,
            "category": category,
            "impact_score": impact_score,
        }

        if deadline:
            meta["deadline"] = deadline
        if tags:
            meta["tags"] = tags

        # Store domain ID for tracking
        if self._domain:
            meta["domain"] = self._domain.id

        content = json.dumps({
            "description": description,
            "category": category,
            "impact_score": impact_score,
        }, sort_keys=True)

        self.ledger.append(
            kind="goal_open",
            content=content,
            meta=meta,
        )

        return goal_id

    def close_goal(
        self,
        goal_id: str,
        outcome: str = "success",
        notes: Optional[str] = None,
    ) -> bool:
        """Close a goal with an outcome.

        Args:
            goal_id: Goal ID to close
            outcome: success, partial, or abandoned
            notes: Optional closing notes

        Returns:
            True if goal was closed, False if not found or already closed
        """
        goal_id = (goal_id or "").strip()
        if not goal_id:
            return False

        if not self._is_goal_open(goal_id):
            return False

        # Validate outcome
        try:
            outcome = GoalOutcome(outcome.lower()).value
        except ValueError:
            outcome = GoalOutcome.SUCCESS.value

        # Get original goal for metrics
        open_event = self._get_open_goal(goal_id)
        if not open_event:
            return False

        # Calculate duration
        open_ts = open_event.get("ts", "")
        duration_days = _days_since(open_ts)

        event_kind = "goal_abandon" if outcome == "abandoned" else "goal_close"

        meta: Dict[str, Any] = {
            "goal_id": goal_id,
            "outcome": outcome,
            "duration_days": round(duration_days, 2),
        }

        if notes:
            meta["notes"] = notes

        content = json.dumps({
            "outcome": outcome,
            "duration_days": round(duration_days, 2),
            "notes": notes,
        }, sort_keys=True)

        self.ledger.append(
            kind=event_kind,
            content=content,
            meta=meta,
        )

        # Record achievement for successful completion
        if outcome == "success":
            self._record_achievement(goal_id, duration_days)

        # Pattern detection is now LAZY for performance optimization.
        # Patterns are analyzed on-demand via:
        # 1. /sparring patterns command
        # 2. Periodic autonomy checks (SparringAutonomy.decide_next_action())
        # 
        # This avoids O(500) ledger scan on every goal close.
        # See: lib/patterns.py, commands/sparring-patterns.md

        return True

    def get_open_goals(self) -> List[Dict[str, Any]]:
        """Get all currently open goals with status info."""
        open_map = self._build_open_map()
        goals = []

        # Get stalled threshold from domain config
        stalled_threshold = 3.0
        if self._domain:
            stalled_threshold = self._domain.get_threshold("stalled_goal_days", 3.0)

        for goal_id, event in sorted(open_map.items(), key=lambda x: x[1].get("id", 0)):
            meta = event.get("meta", {})
            content_str = event.get("content", "{}")
            try:
                content = json.loads(content_str)
            except json.JSONDecodeError:
                content = {}

            age_days = _days_since(event.get("ts", ""))

            goals.append({
                "id": goal_id,
                "description": content.get("description", ""),
                "category": meta.get("category", "other"),
                "opened_at": event.get("ts", ""),
                "age_days": round(age_days, 1),
                "impact_score": meta.get("impact_score", 0),
                "tags": meta.get("tags", []),
                "deadline": meta.get("deadline"),
                "domain": meta.get("domain"),
                "is_stalled": age_days > stalled_threshold,
            })

        return goals

    def get_stalled_goals(self, threshold_days: Optional[float] = None) -> List[Dict[str, Any]]:
        """Get goals without activity beyond the threshold."""
        if threshold_days is None:
            threshold_days = 3.0
            if self._domain:
                threshold_days = self._domain.get_threshold("stalled_goal_days", 3.0)

        open_goals = self.get_open_goals()
        return [g for g in open_goals if g["age_days"] > threshold_days]

    def get_closed_goals(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Get recently closed goals."""
        close_events = self.ledger.read_by_kind("goal_close", limit=limit, reverse=True)
        abandon_events = self.ledger.read_by_kind("goal_abandon", limit=limit, reverse=True)

        all_events = sorted(
            close_events + abandon_events,
            key=lambda e: e.get("id", 0),
            reverse=True
        )[:limit]

        goals = []
        for event in all_events:
            meta = event.get("meta", {})
            content_str = event.get("content", "{}")
            try:
                content = json.loads(content_str)
            except json.JSONDecodeError:
                content = {}

            # Find the original open event
            goal_id = meta.get("goal_id", "")
            open_event = self._find_goal_open_event(goal_id)
            open_content = {}
            if open_event:
                try:
                    open_content = json.loads(open_event.get("content", "{}"))
                except json.JSONDecodeError:
                    pass

            goals.append({
                "id": goal_id,
                "description": open_content.get("description", ""),
                "category": open_content.get("category", "other"),
                "outcome": content.get("outcome", meta.get("outcome", "unknown")),
                "duration_days": content.get("duration_days", 0),
                "closed_at": event.get("ts", ""),
                "notes": content.get("notes"),
            })

        return goals

    def get_goal_stats(self) -> Dict[str, Any]:
        """Calculate goal statistics."""
        open_goals = self.get_open_goals()
        closed_events = self.ledger.read_by_kind("goal_close")
        abandon_events = self.ledger.read_by_kind("goal_abandon")

        total_closed = len(closed_events)
        total_abandoned = len(abandon_events)
        total_completed = total_closed + total_abandoned

        # Completion rate
        completion_rate = (
            total_closed / total_completed if total_completed > 0 else 0.0
        )

        # Average duration for closed goals
        durations = []
        for event in closed_events:
            meta = event.get("meta", {})
            duration = meta.get("duration_days", 0)
            if duration:
                durations.append(duration)

        avg_duration = sum(durations) / len(durations) if durations else 0.0

        # Current streak (consecutive successes)
        streak = self._calculate_streak()

        return {
            "open_count": len(open_goals),
            "total_closed": total_closed,
            "total_abandoned": total_abandoned,
            "completion_rate": round(completion_rate * 100, 1),
            "avg_duration_days": round(avg_duration, 1),
            "current_streak": streak,
            "stalled_count": len([g for g in open_goals if g["is_stalled"]]),
        }

    def prompt_reflection(
        self,
        prompt: Optional[str] = None,
        context: Optional[str] = None,
        goal_ids: Optional[List[str]] = None,
    ) -> str:
        """Create a reflection prompt event.

        Args:
            prompt: Custom reflection prompt (auto-generated if not provided)
            context: Context for the reflection
            goal_ids: Related goal IDs

        Returns:
            Reflection event ID
        """
        from datetime import datetime, timezone

        # Auto-generate prompt if not provided
        if not prompt:
            stats = self.get_goal_stats()
            closed_count = stats["total_closed"]
            if closed_count > 0:
                prompt = f"You've completed {closed_count} goal(s) recently. What patterns do you notice in your work?"
            else:
                prompt = "Take a moment to reflect on your current goals and progress."

        # Create event ID
        event_id = sha1(f"reflection_{datetime.now(timezone.utc).isoformat()}".encode()).hexdigest()[:8]

        content_data = {
            "prompt": prompt,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        meta_data = {
            "reflection_id": event_id,
        }

        if context:
            content_data["context"] = context
            meta_data["context"] = context[:100]

        if goal_ids:
            content_data["goal_ids"] = goal_ids
            meta_data["goal_count"] = len(goal_ids)

        self.ledger.append(
            kind="reflection",
            content=json.dumps(content_data, sort_keys=True),
            meta=meta_data,
        )

        return event_id

    def _is_goal_open(self, goal_id: str) -> bool:
        """Check if a goal is currently open."""
        return goal_id in self._build_open_map()

    def _get_open_goal(self, goal_id: str) -> Optional[Dict[str, Any]]:
        """Get an open goal event by ID."""
        return self._build_open_map().get(goal_id)

    def _build_open_map(self) -> Dict[str, Dict[str, Any]]:
        """Build map of currently open goals.
        
        Uses Mirror for O(1) lookup when available, falls back to O(N) ledger scan.
        """
        # O(1) path: use Mirror if available
        if self._mirror is not None:
            self._mirror.sync()
            return self._mirror.open_goals
        
        # O(N) fallback: scan ledger
        events = self.ledger.read_all()
        opens: Dict[str, Dict[str, Any]] = {}

        for event in events:
            kind = event.get("kind")
            meta = event.get("meta", {})
            goal_id = meta.get("goal_id", "")

            if not goal_id:
                continue

            if kind == "goal_open":
                opens[goal_id] = event
            elif kind in ("goal_close", "goal_abandon"):
                opens.pop(goal_id, None)

        return opens

    def _find_goal_open_event(self, goal_id: str) -> Optional[Dict[str, Any]]:
        """Find the original open event for a goal."""
        events = self.ledger.read_by_kind("goal_open")
        for event in events:
            if event.get("meta", {}).get("goal_id") == goal_id:
                return event
        return None

    def _detect_category(self, description: str) -> str:
        """Detect goal category from description using domain config."""
        if self._domain:
            return self._domain.get_category_by_keywords(description)

        # Legacy fallback for when no domain is loaded
        desc_lower = description.lower()

        legacy_keywords = {
            "bug": ["fix", "bug", "error", "issue", "broken", "crash"],
            "feature": ["add", "implement", "create", "build", "new"],
            "refactor": ["refactor", "clean", "improve", "optimize"],
            "testing": ["test", "spec", "coverage", "e2e", "unit"],
            "documentation": ["doc", "readme", "comment", "guide"],
            "devops": ["deploy", "ci", "cd", "pipeline", "docker"],
            "learning": ["learn", "understand", "study", "explore"],
        }

        for category, keywords in legacy_keywords.items():
            if any(kw in desc_lower for kw in keywords):
                return category

        return "other"

    def _validate_category(self, category: str) -> str:
        """Validate and normalize category against domain config."""
        if self._domain:
            valid_categories = self._domain.get_valid_categories()
            if category in valid_categories:
                return category
            return "other"

        # Legacy validation
        legacy_categories = [
            "feature", "bug", "learning", "refactor",
            "devops", "testing", "documentation", "other"
        ]
        if category in legacy_categories:
            return category
        return "other"

    def _compute_impact_score(self, description: str) -> int:
        """Compute impact score (1-10) based on description."""
        if self._domain:
            return self._domain.compute_impact_score(description)

        # Legacy fallback
        score = 5  # Base score
        desc_lower = description.lower()

        # High impact indicators
        high_impact = ["critical", "urgent", "security", "production", "customer"]
        for word in high_impact:
            if word in desc_lower:
                score += 2

        # Medium impact indicators
        medium_impact = ["important", "needed", "required", "blocker"]
        for word in medium_impact:
            if word in desc_lower:
                score += 1

        # Low impact indicators
        low_impact = ["minor", "nice to have", "cosmetic", "cleanup"]
        for word in low_impact:
            if word in desc_lower:
                score -= 1

        return max(1, min(10, score))

    def _calculate_streak(self) -> int:
        """Calculate current streak of successful goal completions."""
        close_events = self.ledger.read_by_kind("goal_close", reverse=True)
        abandon_events = self.ledger.read_by_kind("goal_abandon", reverse=True)

        # Merge and sort by ID (descending)
        all_events = sorted(
            close_events + abandon_events,
            key=lambda e: e.get("id", 0),
            reverse=True
        )

        streak = 0
        for event in all_events:
            if event.get("kind") == "goal_close":
                meta = event.get("meta", {})
                outcome = meta.get("outcome", "success")
                if outcome == "success":
                    streak += 1
                else:
                    break
            else:
                break  # Abandonment breaks the streak

        return streak

    def _record_achievement(self, goal_id: str, duration_days: float) -> None:
        """Record an achievement for goal completion."""
        stats = self.get_goal_stats()
        streak = stats["current_streak"] + 1  # Include the one just completed

        achievement_type = "goal_completed"
        if streak >= 10:
            achievement_type = "streak_10"
        elif streak >= 5:
            achievement_type = "streak_5"
        elif streak >= 3:
            achievement_type = "streak_3"

        # Use domain threshold for quick win detection
        quick_win_threshold = 1.0
        if self._domain:
            quick_win_threshold = self._domain.get_threshold("quick_win_days", 1.0)

        if duration_days < quick_win_threshold:
            achievement_type = "quick_win"

        meta = {
            "goal_id": goal_id,
            "achievement_type": achievement_type,
            "streak": streak,
        }

        content = json.dumps({
            "type": achievement_type,
            "goal_id": goal_id,
            "streak": streak,
            "duration_days": round(duration_days, 2),
        }, sort_keys=True)

        self.ledger.append(
            kind="achievement",
            content=content,
            meta=meta,
        )


# Legacy compatibility: GoalCategory enum for backward compatibility
class GoalCategory(str, Enum):
    """Legacy category enum - use domain config instead.

    Kept for backward compatibility with existing code.
    """
    FEATURE = "feature"
    BUG = "bug"
    LEARNING = "learning"
    REFACTOR = "refactor"
    DEVOPS = "devops"
    TESTING = "testing"
    DOCUMENTATION = "documentation"
    OTHER = "other"

