"""Behavioral pattern detection for the Conversational Sparring.

Adapted from PMM's rsm.py with domain-agnostic tendency tracking.
Patterns are loaded from domain configuration.
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass
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


@dataclass
class BehavioralPattern:
    """A detected behavioral pattern."""
    name: str
    description: str
    occurrences: int
    trend: str  # "improving", "stable", "declining"
    severity: str  # "info", "warning", "concern"
    suggestion: str
    examples: List[str]


# Legacy pattern definitions - used when no domain config is available
PATTERN_DEFINITIONS = {
    "context_switching": {
        "description": "Starting new goals before completing existing ones",
        "severity_threshold": 3,
        "severity": "warning",
        "suggestion": "Focus on completing one goal before starting another",
    },
    "test_avoidance": {
        "description": "Implementing code without writing tests",
        "severity_threshold": 2,
        "severity": "concern",
        "suggestion": "Consider TDD - write tests first, then implement",
    },
    "review_skipping": {
        "description": "Committing without code review",
        "severity_threshold": 2,
        "severity": "warning",
        "suggestion": "Run /review before committing to catch issues early",
    },
    "goal_abandonment": {
        "description": "Frequently abandoning goals without completion",
        "severity_threshold": 2,
        "severity": "concern",
        "suggestion": "Break large goals into smaller, achievable tasks",
    },
    "rushed_completion": {
        "description": "Closing goals very quickly (< 1 hour)",
        "severity_threshold": 5,
        "severity": "info",
        "suggestion": "Quick wins are good! Make sure quality isn't sacrificed",
    },
    "stalled_work": {
        "description": "Goals sitting idle for extended periods",
        "severity_threshold": 3,
        "severity": "warning",
        "suggestion": "Break blockers into sub-goals or ask for help",
    },
    "reflection_consistency": {
        "description": "Regular reflection on work progress",
        "severity_threshold": 5,
        "severity": "info",
        "suggestion": "Keep reflecting! It helps identify patterns",
    },
}


class PatternDetector:
    """Detect and track behavioral patterns from ledger events.

    Uses domain configuration for pattern definitions and thresholds.
    """

    def __init__(
        self,
        ledger: SparringLedger,
        domain: Optional["DomainConfig"] = None,
        domain_id: Optional[str] = None,
    ) -> None:
        """Initialize PatternDetector.

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
            # Fallback: no domain config (use legacy behavior)
            self._domain = None

        self._pattern_counts: Dict[str, int] = defaultdict(int)
        self._pattern_examples: Dict[str, List[str]] = defaultdict(list)
        self._historical_counts: Dict[str, List[int]] = defaultdict(list)

    @property
    def domain(self) -> Optional["DomainConfig"]:
        """Get current domain configuration."""
        return self._domain

    def _get_pattern_definitions(self) -> Dict[str, Dict[str, Any]]:
        """Get pattern definitions from domain config or legacy fallback."""
        if self._domain:
            return self._domain.patterns
        return PATTERN_DEFINITIONS

    def analyze(self, window: int = 500) -> List[BehavioralPattern]:
        """Analyze recent events for behavioral patterns.

        Args:
            window: Number of recent events to analyze

        Returns:
            List of detected patterns with metadata
        """
        events = self.ledger.read_tail(window)
        self._reset_counts()

        # Process events for pattern detection
        for event in events:
            self._process_event(event, events)

        # Build pattern results
        patterns = []
        pattern_defs = self._get_pattern_definitions()

        for name, definition in pattern_defs.items():
            count = self._pattern_counts[name]
            if count > 0:
                threshold = definition.get("severity_threshold", 3)
                severity = (
                    definition.get("severity", "info")
                    if count >= threshold
                    else "info"
                )
                trend = self._calculate_trend(name)

                patterns.append(BehavioralPattern(
                    name=name,
                    description=definition.get("description", name),
                    occurrences=count,
                    trend=trend,
                    severity=severity,
                    suggestion=definition.get("suggestion", ""),
                    examples=self._pattern_examples[name][:3],
                ))

        # Sort by severity and count
        severity_order = {"concern": 0, "warning": 1, "info": 2}
        patterns.sort(key=lambda p: (severity_order.get(p.severity, 3), -p.occurrences))

        return patterns

    def get_knowledge_gaps(self) -> List[str]:
        """Identify knowledge gaps from struggles and failed attempts."""
        struggles = self.ledger.read_by_kind("struggle")
        gap_counts: Dict[str, int] = defaultdict(int)

        for event in struggles:
            meta = event.get("meta", {})
            topic = meta.get("topic", "general")
            gap_counts[topic] += 1

        # Return topics with multiple struggles
        return sorted(
            [topic for topic, count in gap_counts.items() if count >= 2],
            key=lambda t: gap_counts[t],
            reverse=True
        )

    def get_strengths(self) -> List[str]:
        """Identify user strengths from achievements and patterns."""
        achievements = self.ledger.read_by_kind("achievement")
        closed_goals = self.ledger.read_by_kind("goal_close")

        strengths = []

        # Check for consistency
        if len(achievements) >= 5:
            strengths.append("Consistent goal completion")

        # Check for quick learning
        struggles = self.ledger.read_by_kind("struggle")
        if len(closed_goals) > len(struggles) * 2:
            strengths.append("Efficient problem solving")

        # Check category strengths
        category_success: Dict[str, int] = defaultdict(int)
        for event in closed_goals:
            content_str = event.get("content", "{}")
            try:
                content = json.loads(content_str)
                if content.get("outcome") == "success":
                    open_event = self._find_goal_open(event.get("meta", {}).get("goal_id"))
                    if open_event:
                        open_meta = open_event.get("meta", {})
                        category = open_meta.get("category", "other")
                        category_success[category] += 1
            except json.JSONDecodeError:
                pass

        # Get category names from domain config for nice display
        category_names = {}
        if self._domain:
            category_names = self._domain.get_category_names()

        for category, count in category_success.items():
            if count >= 3:
                display_name = category_names.get(category, category)
                strengths.append(f"Strong at {display_name} tasks")

        return strengths

    def detect_struggle(self, context: str) -> Optional[Dict[str, Any]]:
        """Detect if user is struggling based on context.

        Args:
            context: Recent activity context

        Returns:
            Struggle info dict if detected, None otherwise
        """
        context_lower = context.lower()

        # Use domain-specific struggle indicators if available
        if self._domain:
            indicators = self._domain.struggle_indicators
        else:
            # Legacy indicators
            indicators = {
                "repeated_errors": [
                    "error", "failed", "exception", "traceback",
                    "cannot", "unable", "doesn't work"
                ],
                "confusion": [
                    "confused", "don't understand", "what does",
                    "how do", "why is", "stuck"
                ],
                "time_pressure": [
                    "taking too long", "hours", "been trying",
                    "still not working"
                ],
            }

        detected = []
        for indicator_type, keywords in indicators.items():
            if any(kw in context_lower for kw in keywords):
                detected.append(indicator_type)

        if detected:
            return {
                "indicators": detected,
                "severity": "high" if len(detected) >= 2 else "medium",
                "suggested_action": self._suggest_help(detected),
            }

        return None

    def record_struggle(
        self,
        topic: str,
        indicators: List[str],
        context: Optional[str] = None,
    ) -> int:
        """Record a detected struggle in the ledger."""
        meta = {
            "topic": topic,
            "indicators": indicators,
        }

        content = json.dumps({
            "topic": topic,
            "indicators": indicators,
            "context": context[:200] if context else None,
        }, sort_keys=True)

        return self.ledger.append(
            kind="struggle",
            content=content,
            meta=meta,
        )

    def _reset_counts(self) -> None:
        """Reset pattern counts for fresh analysis."""
        # Save historical for trend calculation
        for name, count in self._pattern_counts.items():
            if count > 0:
                self._historical_counts[name].append(count)
                # Keep only last 5 windows
                self._historical_counts[name] = self._historical_counts[name][-5:]

        self._pattern_counts.clear()
        self._pattern_examples.clear()

    def _process_event(
        self,
        event: Dict[str, Any],
        all_events: List[Dict[str, Any]]
    ) -> None:
        """Process a single event for pattern detection."""
        kind = event.get("kind")
        meta = event.get("meta", {})
        content_str = event.get("content", "")

        # Context switching detection
        if kind == "goal_open":
            open_count = sum(
                1 for e in all_events
                if e.get("kind") == "goal_open"
                and e.get("id", 0) < event.get("id", 0)
            )
            close_count = sum(
                1 for e in all_events
                if e.get("kind") in ("goal_close", "goal_abandon")
                and e.get("id", 0) < event.get("id", 0)
            )
            if open_count > close_count + 2:
                self._pattern_counts["context_switching"] += 1
                try:
                    content = json.loads(content_str)
                    desc = content.get("description", "")[:50]
                    self._pattern_examples["context_switching"].append(
                        f"Started '{desc}' with {open_count - close_count} open goals"
                    )
                except json.JSONDecodeError:
                    pass

        # Goal abandonment detection
        elif kind == "goal_abandon":
            self._pattern_counts["goal_abandonment"] += 1
            goal_id = meta.get("goal_id", "unknown")
            self._pattern_examples["goal_abandonment"].append(
                f"Abandoned goal {goal_id}"
            )

        # Rushed completion detection
        elif kind == "goal_close":
            try:
                content = json.loads(content_str)
                duration = content.get("duration_days", 0)
                # Use domain threshold for quick completion
                quick_threshold = 0.04  # ~1 hour default
                if self._domain:
                    quick_win_days = self._domain.get_threshold("quick_win_days", 1.0)
                    quick_threshold = quick_win_days / 24  # Convert to fraction of day

                if duration < quick_threshold:
                    self._pattern_counts["rushed_completion"] += 1
                    self._pattern_examples["rushed_completion"].append(
                        f"Completed in {round(duration * 24, 1)} hours"
                    )
            except json.JSONDecodeError:
                pass

        # Stalled work detection
        elif kind == "struggle":
            self._pattern_counts["stalled_work"] += 1
            topic = meta.get("topic", "unknown")
            self._pattern_examples["stalled_work"].append(
                f"Struggled with {topic}"
            )

        # Reflection consistency (positive pattern)
        elif kind == "reflection":
            self._pattern_counts["reflection_consistency"] += 1

    def _calculate_trend(self, pattern_name: str) -> str:
        """Calculate trend for a pattern based on historical data."""
        history = self._historical_counts.get(pattern_name, [])
        if len(history) < 2:
            return "stable"

        recent = history[-1] if history else 0
        older_avg = sum(history[:-1]) / len(history[:-1]) if len(history) > 1 else 0

        if recent < older_avg * 0.7:
            return "improving"
        elif recent > older_avg * 1.3:
            return "declining"
        return "stable"

    def _suggest_help(self, indicators: List[str]) -> str:
        """Suggest help based on struggle indicators."""
        suggestions = []

        if "repeated_errors" in indicators:
            suggestions.append("Would you like help debugging?")
        if "confusion" in indicators:
            suggestions.append("I can explain the concept if needed.")
        if "time_pressure" in indicators or "pressure" in indicators:
            suggestions.append("Let's break this into smaller steps.")
        if "blockers" in indicators:
            suggestions.append("Let's identify what's blocking you.")

        return " ".join(suggestions) if suggestions else "How can I help?"

    def _find_goal_open(self, goal_id: str) -> Optional[Dict[str, Any]]:
        """Find the open event for a goal."""
        if not goal_id:
            return None
        events = self.ledger.read_by_kind("goal_open")
        for event in events:
            if event.get("meta", {}).get("goal_id") == goal_id:
                return event
        return None

