"""Recursive Self-Model (RSM) for the Conversational Sparring.

The RSM tracks persistent behavioral tendencies and meta-patterns by analyzing
the Mirror projection and event history. It enables the sparring to "know" the user's
habits and adapt its strategy.
"""

from __future__ import annotations

import json
from typing import Any, Dict, List, Optional, Tuple

from .mirror import SparringMirror


class SparringRSM:
    """Behavioral self-model built from sparring events."""

    # Tendencies to track
    # Format: (trigger_kind, threshold_count, window_size)
    # This is a simplification; real logic is in analyze()
    TENDENCIES = {
        "completion_momentum": "3+ consecutive completions",
        "quick_starter": "High volume of open goals",
        "struggle_prone": "High abandonment rate",
        "reflector": "Regular reflection habit"
    }

    def __init__(self, mirror: SparringMirror) -> None:
        self.mirror = mirror
        self.tendencies: Dict[str, Any] = {}
        self.metrics: Dict[str, Any] = {}

    def analyze(self) -> None:
        """Analyze current state to update self-model."""
        with self.mirror._lock:
            # 1. Calculate basic metrics
            total_goals = len(self.mirror.closed_goals) + len(self.mirror.open_goals)
            closed_count = sum(1 for g in self.mirror.closed_goals.values() if g["status"] == "CLOSED")
            abandoned_count = sum(1 for g in self.mirror.closed_goals.values() if g["status"] == "ABANDONED")
            
            completion_rate = closed_count / total_goals if total_goals > 0 else 0.0
            
            # 2. Detect tendencies
            self.tendencies["struggle_prone"] = abandoned_count > closed_count
            self.tendencies["high_performer"] = completion_rate > 0.8 and total_goals > 5
            
            # 3. Analyze reflection habit
            total_reflections = sum(self.mirror.reflection_counts.values())
            self.tendencies["reflector"] = total_reflections > (total_goals * 0.2)  # Reflected on >20% of work

            # 4. Check for momentum (last 3 events were goal_close)
            # This requires checking the ledger history, which is expensive in aggregate,
            # but we can check the tail from the ledger via mirror (if we added tail access to mirror)
            # For now, we'll use a simplified heuristic based on recent events if available, 
            # or relying on the mirror's aggregate stats.
            
            # Let's peek at the last few events from the ledger
            try:
                recent = self.mirror.ledger.read_tail(limit=5)
                closes_in_row = 0
                for ev in reversed(recent):
                    if ev["kind"] == "goal_close":
                        closes_in_row += 1
                    elif ev["kind"] in ("goal_open", "struggle"):
                        break
                self.tendencies["completion_momentum"] = closes_in_row >= 3
            except Exception:
                pass

            self.metrics = {
                "completion_rate": completion_rate,
                "total_goals": total_goals,
                "abandoned_count": abandoned_count
            }

    def snapshot(self) -> Dict[str, Any]:
        """Return a serializable snapshot of the self-model."""
        self.analyze()  # Ensure fresh
        return {
            "tendencies": self.tendencies,
            "metrics": self.metrics,
            "current_domain": self.mirror.current_domain
        }

    def publish_snapshot(self) -> int:
        """Emit an rsm_snapshot event to the ledger."""
        data = self.snapshot()
        return self.mirror.ledger.append(
            kind="rsm_snapshot",
            content=json.dumps(data)
        )

