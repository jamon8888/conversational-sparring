"""Cognitive logic for the Hybrid Sparring System (v5.1).

Implements the "Dual Process" architecture:
1. Decision Mode (Debiasing, Strategy)
2. Learning Mode (Cognitive Apprenticeship, ERE)

Tracks state via the ledger using `cognitive_mode_switch` and `ere_adjustment` events.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple

try:
    from .ledger import SparringLedger
except ImportError:
    from ledger import SparringLedger


class CognitiveMode(str, Enum):
    """The two primary operating modes."""
    DECISION = "decision"
    LEARNING = "learning"


class ERELevel(int, Enum):
    """ERE (Element Interactivity) levels for Learning Mode."""
    NOVICE = 1    # High support (Modeling)
    ADVANCED = 2  # Medium support (Scaffolding)
    COMPETENT = 3 # Low support (Exploration)
    AUTONOMOUS = 4 # Graduation


@dataclass
class CognitiveState:
    """Current cognitive state of the session."""
    mode: CognitiveMode
    ere_level: ERELevel
    confidence: float
    automation_bias_check: bool
    context: str


class CognitiveRouter:
    """Decides between Decision and Learning modes based on user intent."""

    def __init__(self, ledger: SparringLedger) -> None:
        self.ledger = ledger

    def determine_mode(self, text: str) -> Tuple[CognitiveMode, float]:
        """Analyze text to determine the appropriate cognitive mode.
        
        Logic from SYSTEM_PROMPT_HYBRIDE_v5.1.md:
        
        DECISION if:
        - "should I", "hesitating", "what do you think", "good idea?"
        - Choice between options, identified stakes
        
        LEARNING if:
        - "how to", "starting", "want to learn", "show me"
        - Skill to develop, first exposure
        """
        text_lower = text.lower()
        
        # Decision triggers
        decision_keywords = [
            "should i", "should we", "hesitating", "option", "choice", 
            "decide", "decision", "risk", "tradeoff", "vs", "versus",
            "opinion", "feedback on plan"
        ]
        
        # Learning triggers
        learning_keywords = [
            "how to", "how do i", "teach me", "show me", "explain",
            "learn", "start", "understand", "beginner", "new to",
            "guide", "tutorial", "example"
        ]
        
        decision_score = sum(1 for w in decision_keywords if w in text_lower)
        learning_score = sum(1 for w in learning_keywords if w in text_lower)
        
        # Default to previous mode if ambiguous, or Learning if completely new
        if decision_score > learning_score:
            return CognitiveMode.DECISION, 0.8
        elif learning_score > decision_score:
            return CognitiveMode.LEARNING, 0.8
        else:
            # Fallback/Ambiguous
            return CognitiveMode.LEARNING, 0.4

    def get_current_ere_level(self) -> ERELevel:
        """Calculate current ERE level based on history.
        
        New users start at NOVICE (1).
        Users with >10 successful completions move to ADVANCED (2).
        Users with >25 successful completions move to COMPETENT (3).
        """
        # Read recent achievements and completions
        completions = self.ledger.count_by_kind("goal_close")
        
        if completions > 25:
            return ERELevel.COMPETENT
        elif completions > 10:
            return ERELevel.ADVANCED
        else:
            return ERELevel.NOVICE

    def record_switch(self, mode: CognitiveMode, reason: str) -> int:
        """Record a mode switch event."""
        content = json.dumps({
            "mode": mode.value,
            "reason": reason
        })
        return self.ledger.append(
            kind="cognitive_mode_switch",
            content=content,
            meta={"mode": mode.value}
        )

    def record_ere_adjustment(self, level: ERELevel, reason: str) -> int:
        """Record an ERE level adjustment."""
        content = json.dumps({
            "level": level.value,
            "reason": reason
        })
        return self.ledger.append(
            kind="ere_adjustment",
            content=content,
            meta={"level": level.value}
        )
