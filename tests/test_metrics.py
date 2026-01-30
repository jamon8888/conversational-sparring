
import pytest
from metrics import calculate_metrics, get_progress_summary
from goals import GoalManager

class TestMetrics:
    """Test the metrics module."""

    def test_empty_metrics(self, ledger):
        """Test metrics on empty ledger."""
        metrics = calculate_metrics(ledger)

        assert metrics.goal_completion_rate == 0.0
        assert metrics.streak_current == 0

    def test_completion_rate(self, ledger):
        """Test completion rate calculation."""
        manager = GoalManager(ledger)

        # Create goals with mixed outcomes
        g1 = manager.open_goal("Goal 1")
        g2 = manager.open_goal("Goal 2")
        g3 = manager.open_goal("Goal 3")
        g4 = manager.open_goal("Goal 4")

        manager.close_goal(g1, outcome="success")
        manager.close_goal(g2, outcome="success")
        manager.close_goal(g3, outcome="success")
        manager.close_goal(g4, outcome="abandoned")

        metrics = calculate_metrics(ledger)

        # 3 out of 4 = 75%
        assert metrics.goal_completion_rate == 75.0

    def test_progress_summary(self, ledger):
        """Test progress summary generation."""
        manager = GoalManager(ledger)

        for i in range(5):
            g = manager.open_goal(f"Goal {i}")
            manager.close_goal(g, outcome="success")

        summary = get_progress_summary(ledger)

        assert "status" in summary
        assert "metrics" in summary
        assert "insights" in summary
