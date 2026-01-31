"""Unified SparringState facade for O(1) dashboard operations.

This module provides a single entry point for all sparring state queries,
eliminating redundant calculations across Mirror, RSM, Autonomy, and Cognition.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from .ledger import SparringLedger
from .mirror import SparringMirror
from .rsm import SparringRSM
from .autonomy import SparringAutonomy
from .cognition import CognitiveRouter, CognitiveMode, ERELevel


class SparringState:
    """Central facade for all sparring state operations.
    
    Provides O(1) access to dashboard data by coordinating:
    - Mirror (in-memory projection)
    - RSM (behavioral tendencies)
    - Autonomy (proactive decisions)
    - Cognition (mode detection)
    
    Usage:
        state = SparringState(ledger)
        dashboard = state.get_dashboard()
    """

    def __init__(self, ledger: SparringLedger) -> None:
        """Initialize state facade.
        
        Args:
            ledger: The sparring ledger instance
        """
        self.ledger = ledger
        self.mirror = SparringMirror(ledger)
        self.rsm = SparringRSM(self.mirror)
        self.autonomy = SparringAutonomy(ledger)
        self.cognition = CognitiveRouter(ledger)
        
        # Initial rebuild
        self.mirror.rebuild()

    def get_dashboard(self) -> Dict[str, Any]:
        """Get complete dashboard state in O(1).
        
        Returns:
            Dict with stats, tendencies, decision, and cognitive mode
        """
        # Sync to latest events
        self.mirror.sync()
        self.rsm.analyze()
        
        # Get autonomy decision
        decision = self.autonomy.decide_next_action()
        
        # Get cognitive state
        ere_level = self.cognition.get_current_ere_level()
        last_mode = self._get_last_mode()
        
        return {
            "stats": self.mirror.get_stats(),
            "tendencies": self.rsm.tendencies,
            "metrics": self.rsm.metrics,
            "decision": decision.to_dict(),
            "ere_level": ere_level.value,
            "ere_name": ere_level.name,
            "mode": last_mode,
            "domain": self.mirror.current_domain,
        }

    def get_quick_status(self) -> Dict[str, Any]:
        """Get minimal status for quick checks.
        
        Returns:
            Dict with open_goals_count, domain, and decision action
        """
        self.mirror.sync()
        decision = self.autonomy.decide_next_action()
        
        return {
            "open_goals": len(self.mirror.open_goals),
            "domain": self.mirror.current_domain,
            "action": decision.action,
        }

    def _get_last_mode(self) -> str:
        """Get the last cognitive mode from ledger."""
        event = self.ledger.last_of_kind("cognitive_mode_switch")
        if event:
            meta = event.get("meta", {})
            return meta.get("mode", "learning")
        return "learning"

    def refresh(self) -> None:
        """Force full refresh of all state."""
        self.mirror.rebuild()
        self.rsm.analyze()
