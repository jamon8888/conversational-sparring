"""Conversational Sparring library modules.

Core components for persistent, personalized developer sparring.
"""

from .ledger import SparringLedger, EVENT_KINDS, get_default_db_path
from .goals import GoalManager, GoalCategory, GoalOutcome
from .patterns import PatternDetector, BehavioralPattern, PATTERN_DEFINITIONS
from .feedback import FeedbackGenerator, FeedbackItem, FeedbackSeverity
from .metrics import (
    SparringMetrics,
    calculate_metrics,
    get_progress_summary,
    format_metrics_display,
)

__all__ = [
    # Ledger
    "SparringLedger",
    "EVENT_KINDS",
    "get_default_db_path",
    # Goals
    "GoalManager",
    "GoalCategory",
    "GoalOutcome",
    # Patterns
    "PatternDetector",
    "BehavioralPattern",
    "PATTERN_DEFINITIONS",
    # Feedback
    "FeedbackGenerator",
    "FeedbackItem",
    "FeedbackSeverity",
    # Metrics
    "SparringMetrics",
    "calculate_metrics",
    "get_progress_summary",
    "format_metrics_display",
]

