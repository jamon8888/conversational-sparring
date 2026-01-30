
import pytest
from feedback import FeedbackGenerator
from goals import GoalManager

class TestFeedbackGenerator:
    """Test the FeedbackGenerator class."""

    def test_reflection_recording(self, ledger):
        """Test recording reflections."""
        feedback = FeedbackGenerator(ledger)

        event_id = feedback.record_reflection(
            intent="Implement auth",
            outcome="Got tokens working",
            next_action="Add refresh flow",
        )

        assert event_id > 0
        reflections = ledger.read_by_kind("reflection")
        assert len(reflections) == 1

    def test_post_work_feedback(self, ledger):
        """Test generating post-work feedback."""
        manager = GoalManager(ledger)
        feedback = FeedbackGenerator(ledger)

        goal_id = manager.open_goal("Test goal")
        manager.close_goal(goal_id)

        result = feedback.generate_post_work_feedback()

        assert "summary" in result
        assert "feedback" in result
