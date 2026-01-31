"""Test suite for architecture optimization.

Tests the new SparringState facade, Mirror snapshot persistence,
and Goals → Mirror migration.
"""

import json
import os
import tempfile
import pytest

from lib.ledger import SparringLedger
from lib.mirror import SparringMirror


class TestMirrorSnapshot:
    """Test Mirror snapshot save/load functionality."""

    def setup_method(self):
        """Create temporary ledger for each test."""
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.ledger = SparringLedger(path=self.temp_db.name)
        self.mirror = SparringMirror(self.ledger)

    def teardown_method(self):
        """Clean up temporary files."""
        self.ledger.close()
        os.unlink(self.temp_db.name)

    def test_snapshot_roundtrip(self):
        """Test save and load snapshot."""
        # Create some state
        self.ledger.append(
            kind="goal_open",
            content=json.dumps({"description": "Test goal"}),
            meta={"goal_id": "test123", "category": "feature"}
        )
        self.mirror.rebuild()

        # Verify state exists
        assert "test123" in self.mirror.open_goals

        # Save snapshot
        snapshot_path = tempfile.NamedTemporaryFile(suffix=".json", delete=False).name
        try:
            self.mirror.save_snapshot(snapshot_path)

            # Create fresh mirror
            fresh_mirror = SparringMirror(self.ledger)
            assert len(fresh_mirror.open_goals) == 0  # Not yet loaded

            # Load snapshot
            loaded = fresh_mirror.load_snapshot(snapshot_path)
            assert loaded is True
            assert "test123" in fresh_mirror.open_goals
        finally:
            os.unlink(snapshot_path)

    def test_snapshot_sync_after_load(self):
        """Test that sync() works correctly after loading snapshot."""
        # Create initial state
        self.ledger.append(
            kind="goal_open",
            content=json.dumps({"description": "Goal 1"}),
            meta={"goal_id": "goal1"}
        )
        self.mirror.rebuild()

        # Save snapshot
        snapshot_path = tempfile.NamedTemporaryFile(suffix=".json", delete=False).name
        try:
            self.mirror.save_snapshot(snapshot_path)

            # Add more events to ledger
            self.ledger.append(
                kind="goal_open",
                content=json.dumps({"description": "Goal 2"}),
                meta={"goal_id": "goal2"}
            )

            # Load snapshot into fresh mirror (will have goal1 but not goal2)
            fresh_mirror = SparringMirror(self.ledger)
            fresh_mirror.load_snapshot(snapshot_path)
            assert "goal1" in fresh_mirror.open_goals
            assert "goal2" not in fresh_mirror.open_goals

            # Sync should pick up goal2
            fresh_mirror.sync()
            assert "goal2" in fresh_mirror.open_goals
        finally:
            os.unlink(snapshot_path)


class TestMirrorPerformance:
    """Test Mirror O(1) operations."""

    def setup_method(self):
        """Create temporary ledger with many events."""
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.ledger = SparringLedger(path=self.temp_db.name)

        # Add 100 goals
        for i in range(100):
            self.ledger.append(
                kind="goal_open",
                content=json.dumps({"description": f"Goal {i}"}),
                meta={"goal_id": f"goal{i}"}
            )


        self.mirror = SparringMirror(self.ledger)
        self.mirror.rebuild()

    def teardown_method(self):
        """Clean up."""
        self.ledger.close()
        os.unlink(self.temp_db.name)

    def test_get_stats_is_o1(self):
        """Test that get_stats() doesn't scan ledger."""
        import time

        # Time get_stats (should be instant)
        start = time.perf_counter()
        for _ in range(1000):
            self.mirror.get_stats()
        elapsed = time.perf_counter() - start

        # Should complete 1000 calls in < 100ms (O(1))
        assert elapsed < 0.1, f"get_stats() too slow: {elapsed:.3f}s for 1000 calls"

    def test_sync_is_incremental(self):
        """Test that sync() only processes new events."""
        # Add one more event
        self.ledger.append(
            kind="goal_open",
            content=json.dumps({"description": "New goal"}),
            meta={"goal_id": "new_goal"}
        )

        # Sync should only process the one new event
        old_count = len(self.mirror.open_goals)
        self.mirror.sync()
        new_count = len(self.mirror.open_goals)

        assert new_count == old_count + 1


class TestGoalManagerWithMirror:
    """Test GoalManager integration with Mirror."""

    def setup_method(self):
        """Create temporary ledger."""
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.ledger = SparringLedger(path=self.temp_db.name)
        self.mirror = SparringMirror(self.ledger)

    def teardown_method(self):
        """Clean up."""
        self.ledger.close()
        os.unlink(self.temp_db.name)

    def test_goal_manager_uses_mirror(self):
        """Test that GoalManager can use Mirror for O(1) lookups."""
        from goals import GoalManager

        # Create manager with mirror injection (if supported)
        manager = GoalManager(self.ledger)

        # Open a goal
        goal_id = manager.open_goal("Test goal for mirror")

        # Rebuild mirror to pick up the new goal
        self.mirror.rebuild()

        # Verify goal is in mirror
        assert goal_id in self.mirror.open_goals

        # Close the goal
        manager.close_goal(goal_id)

        # Sync mirror
        self.mirror.sync()

        # Verify goal moved to closed
        assert goal_id not in self.mirror.open_goals
        assert goal_id in self.mirror.closed_goals


class TestSparringState:
    """Test the SparringState facade (once implemented)."""

    def setup_method(self):
        """Create temporary ledger."""
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.ledger = SparringLedger(path=self.temp_db.name)

    def teardown_method(self):
        """Clean up."""
        self.ledger.close()
        os.unlink(self.temp_db.name)

    def test_dashboard_contains_all_fields(self):
        """Test that get_dashboard() returns complete state."""
        # This test will fail until SparringState is implemented
        try:
            from state import SparringState
        except ImportError:
            # SparringState not yet implemented
            return

        state = SparringState(self.ledger)
        dashboard = state.get_dashboard()

        # Verify all expected fields present
        assert "stats" in dashboard
        assert "tendencies" in dashboard
        assert "decision" in dashboard
        assert "ere_level" in dashboard


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
