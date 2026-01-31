"""Progress and efficiency metrics for the Conversational Sparring system.

Adapted from PMM's efficiency_metrics.py with domain-aware thresholds.
"""

from __future__ import annotations

import json
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
class SparringMetrics:
    """Aggregated sparring metrics."""
    goal_completion_rate: float  # Percentage of goals completed successfully
    avg_goal_duration_days: float  # Average time to complete a goal
    struggle_frequency: float  # Struggles per goal
    reflection_rate: float  # Reflections per goal
    streak_current: int  # Current success streak
    streak_best: int  # Best success streak
    total_goals_completed: int
    total_goals_abandoned: int
    learning_velocity: float  # Improvement rate (positive = improving)
    ere_level: int = 1  # Element Interactivity Level (1-4)
    sdt_scores: Dict[str, float] = None  # Autonomy/Competence/Relatedness (0-10)


def calculate_metrics(
    ledger: SparringLedger,
    window: int = 500,
    domain: Optional["DomainConfig"] = None,  # noqa: ARG001 - reserved for future use
) -> SparringMetrics:
    """Calculate comprehensive sparring metrics.

    Args:
        ledger: Sparring ledger instance
        window: Number of events to analyze
        domain: Optional domain config for threshold customization

    Returns:
        SparringMetrics dataclass
    """
    events = ledger.read_tail(max(1, window))

    # Count event types
    goal_opens = [e for e in events if e.get("kind") == "goal_open"]
    goal_closes = [e for e in events if e.get("kind") == "goal_close"]
    goal_abandons = [e for e in events if e.get("kind") == "goal_abandon"]
    struggles = [e for e in events if e.get("kind") == "struggle"]
    reflections = [e for e in events if e.get("kind") == "reflection"]

    # Goal completion rate
    total_resolved = len(goal_closes) + len(goal_abandons)
    completion_rate = (
        len(goal_closes) / total_resolved * 100
        if total_resolved > 0 else 0.0
    )

    # Average duration
    durations = []
    for event in goal_closes:
        try:
            content = json.loads(event.get("content", "{}"))
            duration = content.get("duration_days", 0)
            if duration:
                durations.append(duration)
        except json.JSONDecodeError:
            pass

    avg_duration = sum(durations) / len(durations) if durations else 0.0

    # Struggle frequency
    struggle_freq = (
        len(struggles) / len(goal_opens)
        if goal_opens else 0.0
    )

    # Reflection rate
    reflection_rate = (
        len(reflections) / len(goal_opens)
        if goal_opens else 0.0
    )

    # Calculate streaks
    current_streak, best_streak = _calculate_streaks(goal_closes, goal_abandons)

    # Learning velocity (compare first half to second half)
    learning_velocity = _calculate_learning_velocity(events)

    # ERE Level
    ere_level = 1
    ere_events = [e for e in events if e.get("kind") == "ere_adjustment"]
    if ere_events:
        try:
            latest_ere = json.loads(ere_events[-1].get("content", "{}"))
            ere_level = int(latest_ere.get("level", 1))
        except (json.JSONDecodeError, ValueError):
            pass

    # SDT Scores
    sdt_scores = {"autonomy": 5.0, "competence": 5.0, "relatedness": 5.0}
    sdt_events = [e for e in events if e.get("kind") == "sdt_assessment"]
    if sdt_events:
        try:
            latest_sdt = json.loads(sdt_events[-1].get("content", "{}"))
            sdt_scores = {
                "autonomy": float(latest_sdt.get("autonomy", 5.0)),
                "competence": float(latest_sdt.get("competence", 5.0)),
                "relatedness": float(latest_sdt.get("relatedness", 5.0)),
            }
        except (json.JSONDecodeError, ValueError):
            pass

    return SparringMetrics(
        goal_completion_rate=round(completion_rate, 1),
        avg_goal_duration_days=round(avg_duration, 2),
        struggle_frequency=round(struggle_freq, 2),
        reflection_rate=round(reflection_rate, 2),
        streak_current=current_streak,
        streak_best=best_streak,
        total_goals_completed=len(goal_closes),
        total_goals_abandoned=len(goal_abandons),
        learning_velocity=round(learning_velocity, 2),
        ere_level=ere_level,
        sdt_scores=sdt_scores,
    )


def _calculate_streaks(
    closes: List[Dict[str, Any]],
    abandons: List[Dict[str, Any]],
) -> tuple:
    """Calculate current and best success streaks."""
    # Combine and sort by ID
    all_resolved = sorted(
        [("close", e) for e in closes] + [("abandon", e) for e in abandons],
        key=lambda x: x[1].get("id", 0),
    )

    current_streak = 0
    best_streak = 0
    temp_streak = 0

    for event_type, event in all_resolved:
        if event_type == "close":
            # Check if successful
            try:
                content = json.loads(event.get("content", "{}"))
                outcome = content.get("outcome", "success")
            except json.JSONDecodeError:
                outcome = "success"

            if outcome == "success":
                temp_streak += 1
                best_streak = max(best_streak, temp_streak)
            else:
                temp_streak = 0
        else:
            temp_streak = 0

    # Current streak is from the end
    current_streak = 0
    for event_type, event in reversed(all_resolved):
        if event_type == "close":
            try:
                content = json.loads(event.get("content", "{}"))
                outcome = content.get("outcome", "success")
            except json.JSONDecodeError:
                outcome = "success"

            if outcome == "success":
                current_streak += 1
            else:
                break
        else:
            break

    return current_streak, best_streak


def _calculate_learning_velocity(events: List[Dict[str, Any]]) -> float:
    """Calculate learning velocity by comparing early vs late performance.

    Positive value means improving, negative means declining.
    """
    if len(events) < 20:
        return 0.0

    midpoint = len(events) // 2
    first_half = events[:midpoint]
    second_half = events[midpoint:]

    def struggle_rate(event_list: List[Dict]) -> float:
        struggles = sum(1 for e in event_list if e.get("kind") == "struggle")
        goals = sum(1 for e in event_list if e.get("kind") == "goal_open")
        return struggles / goals if goals > 0 else 0.0

    first_rate = struggle_rate(first_half)
    second_rate = struggle_rate(second_half)

    # Positive velocity means fewer struggles over time
    return (first_rate - second_rate) * 100


def get_progress_summary(
    ledger: SparringLedger,
    domain: Optional["DomainConfig"] = None,
    domain_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Generate a human-readable progress summary.

    Args:
        ledger: Sparring ledger instance
        domain: Optional pre-loaded domain config
        domain_id: Optional domain ID to load

    Returns:
        Dict with summary information
    """
    # Load domain config if not provided
    if domain is None and domain_id is not None and load_domain is not None:
        domain = load_domain(domain_id)
    elif domain is None and load_domain is not None and get_default_domain is not None:
        domain = load_domain(get_default_domain())

    metrics = calculate_metrics(ledger, domain=domain)

    # Determine overall status
    if metrics.goal_completion_rate >= 80:
        status = "excellent"
        status_message = "You're crushing it!"
    elif metrics.goal_completion_rate >= 60:
        status = "good"
        status_message = "Solid progress!"
    elif metrics.goal_completion_rate >= 40:
        status = "moderate"
        status_message = "Room for improvement"
    else:
        status = "needs_attention"
        status_message = "Let's work on consistency"

    # Build insights
    insights = []

    if metrics.streak_current >= 5:
        # Use domain message template if available
        if domain:
            streak_msg = domain.get_message("streak_message", "{count}-goal success streak")
            streak_msg = streak_msg.replace("{count}", str(metrics.streak_current))
            insights.append(f"On fire! {streak_msg}")
        else:
            insights.append(f"On fire! {metrics.streak_current}-goal success streak")
    elif metrics.streak_current >= 3:
        insights.append(f"Building momentum: {metrics.streak_current}-goal streak")

    if metrics.struggle_frequency > 1:
        insights.append("Encountering frequent challenges - consider breaking goals smaller")
    elif metrics.struggle_frequency < 0.3:
        insights.append("Smooth sailing - goals are well-scoped")

    if metrics.reflection_rate >= 1:
        insights.append("Great reflection habits!")
    elif metrics.reflection_rate < 0.5:
        insights.append("Consider reflecting more often with /sparring reflect")

    if metrics.learning_velocity > 10:
        insights.append("Clear improvement trend - fewer struggles over time")
    elif metrics.learning_velocity < -10:
        insights.append("Struggling more recently - might need a different approach")

    # Add domain-specific context
    domain_name = domain.name if domain else "General"

    return {
        "status": status,
        "status_message": status_message,
        "domain": domain_name,
        "metrics": {
            "completion_rate": f"{metrics.goal_completion_rate}%",
            "avg_duration": f"{metrics.avg_goal_duration_days} days",
            "current_streak": metrics.streak_current,
            "best_streak": metrics.streak_best,
            "total_completed": metrics.total_goals_completed,
            "total_abandoned": metrics.total_goals_abandoned,
        },
        "insights": insights,
    }


def format_metrics_display(
    metrics: SparringMetrics,
    domain: Optional["DomainConfig"] = None,
) -> str:
    """Format metrics for CLI display.

    Args:
        metrics: Calculated metrics
        domain: Optional domain config for customization

    Returns:
        Formatted string for display
    """
    domain_name = domain.name if domain else "General"

    lines = [
        "## Sparring Metrics",
        f"**Domain:** {domain_name}",
        "",
        f"**Completion Rate:** {metrics.goal_completion_rate}%",
        f"**Avg Duration:** {metrics.avg_goal_duration_days} days",
        f"**Current Streak:** {metrics.streak_current}",
        f"**Best Streak:** {metrics.streak_best}",
        "",
        f"Goals Completed: {metrics.total_goals_completed}",
        f"Goals Abandoned: {metrics.total_goals_abandoned}",
        "",
        f"Struggle Frequency: {metrics.struggle_frequency} per goal",
        f"Reflection Rate: {metrics.reflection_rate} per goal",
        f"Learning Velocity: {'+' if metrics.learning_velocity >= 0 else ''}{metrics.learning_velocity}%",
    ]

    return "\n".join(lines)


def get_domain_thresholds(domain: Optional["DomainConfig"]) -> Dict[str, Any]:
    """Get all domain-specific thresholds.

    Args:
        domain: Domain config or None for defaults

    Returns:
        Dict of threshold values
    """
    defaults = {
        "stalled_goal_days": 3,
        "quick_win_days": 1,
        "max_open_goals": 7,
        "reflection_cadence": "daily",
    }

    if domain is None:
        return defaults

    return {
        key: domain.get_threshold(key, default)
        for key, default in defaults.items()
    }

