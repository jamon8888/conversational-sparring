"""Autonomy Kernel for the Conversational Sparring.

The Autonomy Kernel enables the sparring to act proactively by analyzing the
current state and deciding if an intervention is needed (e.g., prompting
reflection, offering help, celebrating milestones).
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from .mirror import SparringMirror
from .rsm import SparringRSM


@dataclass
class SparringDecision:
    """A proactive decision made by the autonomy kernel."""
    action: str  # reflect, intervene, celebrate, idle
    reason: str
    evidence: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "action": self.action,
            "reason": self.reason,
            "evidence": self.evidence
        }


class SparringAutonomy:
    """Deterministic self-direction for the sparring."""

    DEFAULT_THRESHOLDS = {
        "reflection_prompt_interval": 5,    # Goals closed before prompt
        "stalled_goal_days": 7,             # Days inactive before check-in
        "struggle_threshold": 2,            # Abandoned goals to trigger help
    }

    def __init__(
        self,
        mirror: SparringMirror,
        rsm: SparringRSM,
        thresholds: Optional[Dict[str, int]] = None
    ) -> None:
        self.mirror = mirror
        self.rsm = rsm
        self.thresholds = {**self.DEFAULT_THRESHOLDS, **(thresholds or {})}

    def decide_next_action(self) -> SparringDecision:
        """Decide the next proactive action based on current state."""
        # Ensure fresh state
        self.mirror.sync()
        self.rsm.analyze()

        # Priority 1: Check for struggles (Intervention)
        if self._check_struggle():
            return SparringDecision(
                action="intervene",
                reason="Detected struggle pattern",
                evidence=["struggle_prone_tendency"]
            )

        # Priority 2: Check for stalled goals (Check-in)
        stalled = self._check_stalled_goals()
        if stalled:
            return SparringDecision(
                action="check_in",
                reason="Goals appear stalled",
                evidence=stalled
            )

        # Priority 3: Check for reflection due (Reflection)
        if self._check_reflection_due():
            return SparringDecision(
                action="reflect",
                reason="Reflection due after recent progress",
                evidence=["goal_completion_threshold_met"]
            )

        return SparringDecision(action="idle", reason="No action needed")

    def _check_struggle(self) -> bool:
        """Return True if intervention is needed."""
        return self.rsm.tendencies.get("struggle_prone", False)

    def _check_stalled_goals(self) -> List[str]:
        """Return list of IDs of goals that are stalled."""
        stalled_ids = []
        now = datetime.now(timezone.utc)
        
        limit_days = self.thresholds["stalled_goal_days"]

        for goal_id, goal in self.mirror.open_goals.items():
            # Parse created_at ISO string
            try:
                # Handle varying ISO formats if needed, but assuming standard
                created_at = datetime.fromisoformat(goal["created_at"].replace("Z", "+00:00"))
                delta = now - created_at
                if delta.days >= limit_days:
                    stalled_ids.append(goal_id)
            except (ValueError, TypeError):
                continue

        return stalled_ids

    def _check_reflection_due(self) -> bool:
        """Return True if a reflection is recommended."""
        # Logic: If (total_closed - total_reflections * interval) > interval
        # Basic heuristic: Have we closed enough goals since the last implied reflection?
        
        total_closed = len(self.mirror.closed_goals)
        total_reflections = sum(self.mirror.reflection_counts.values())
        interval = self.thresholds["reflection_prompt_interval"]

        # If zero reflections, check if we simply passed the interval
        if total_reflections == 0:
            return total_closed >= interval

        # Otherwise, check ratio/gap
        # e.g. 12 closed, 2 reflections. 12 / 2 = 6. If interval is 5, maybe due?
        # Better: simple subtraction of 'unreflected' work
        # This is an approximation since we don't link specific reflections to specific goals yet.
        return (total_closed - (total_reflections * interval)) >= interval

