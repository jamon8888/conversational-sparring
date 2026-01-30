
import pytest
from goals import GoalManager, GoalCategory
from ledger import SparringLedger

class TestGoalManager:
    """Test the GoalManager class."""

    def test_open_goal(self, ledger):
        """Test opening a goal."""
        manager = GoalManager(ledger)

        goal_id = manager.open_goal("Implement user authentication")

        assert goal_id is not None
        assert len(goal_id) == 8

        goals = manager.get_open_goals()
        assert len(goals) == 1
        assert goals[0]["id"] == goal_id

    def test_close_goal(self, ledger):
        """Test closing a goal."""
        manager = GoalManager(ledger)

        goal_id = manager.open_goal("Test goal")
        success = manager.close_goal(goal_id, outcome="success")

        assert success is True

        open_goals = manager.get_open_goals()
        assert len(open_goals) == 0

        closed_goals = manager.get_closed_goals()
        assert len(closed_goals) == 1

    def test_automatic_category_detection(self, ledger):
        """Test automatic category detection (generic)."""
        manager = GoalManager(ledger)

        # "Fix" keyword -> bug
        manager.open_goal("Fix broken redirect")
        goals = manager.get_open_goals()
        assert goals[0]["category"] == "bug"

    def test_goal_stats(self, ledger):
        """Test goal statistics calculation."""
        manager = GoalManager(ledger)

        g1 = manager.open_goal("Goal 1")
        g2 = manager.open_goal("Goal 2")
        
        manager.close_goal(g1, outcome="success")
        manager.close_goal(g2, outcome="abandoned")

        stats = manager.get_goal_stats()

        assert stats["total_closed"] == 1
        assert stats["total_abandoned"] == 1
        assert stats["completion_rate"] == 50.0
