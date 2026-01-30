
import pytest
from patterns import PatternDetector, PATTERN_DEFINITIONS
from goals import GoalManager

class TestPatternDetector:
    """Test the PatternDetector class."""

    def test_empty_ledger(self, ledger):
        """Test pattern detection on empty ledger."""
        detector = PatternDetector(ledger)
        patterns = detector.analyze()
        assert isinstance(patterns, list)

    def test_context_switching_detection(self, ledger):
        """Test context switching pattern detection."""
        manager = GoalManager(ledger)
        detector = PatternDetector(ledger)

        # Open many goals without closing
        for i in range(5):
            manager.open_goal(f"Goal {i}")

        patterns = detector.analyze()
        pattern_names = [p.name for p in patterns]

        assert "context_switching" in pattern_names

    def test_struggle_recording(self, ledger):
        """Test recording struggles."""
        detector = PatternDetector(ledger)

        event_id = detector.record_struggle(
            topic="async-patterns",
            indicators=["repeated_errors"],
            context="Confused about Promise chains",
        )

        assert event_id > 0
        struggles = ledger.read_by_kind("struggle")
        assert len(struggles) == 1

    def test_knowledge_gaps(self, ledger):
        """Test knowledge gap detection."""
        detector = PatternDetector(ledger)

        for _ in range(3):
            detector.record_struggle(
                topic="typescript-generics",
                indicators=["confusion"],
            )

        gaps = detector.get_knowledge_gaps()
        assert "typescript-generics" in gaps
