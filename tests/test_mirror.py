"""Tests for the Mirror Projection Layer."""

import json
import os
import tempfile
import pytest

from lib.ledger import SparringLedger
from lib.mirror import SparringMirror


@pytest.fixture
def temp_ledger():
    """Create a temporary ledger for testing."""
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    ledger = SparringLedger(path)
    yield ledger
    ledger.close()
    os.unlink(path)


def test_mirror_init(temp_ledger):
    """Test that mirror initializes with empty state."""
    mirror = SparringMirror(temp_ledger)
    assert mirror.open_goals == {}
    assert mirror.current_domain == "developer"
    assert mirror.last_event_id == 0


def test_goal_lifecycle(temp_ledger):
    """Test standard goal open -> close cycle."""
    mirror = SparringMirror(temp_ledger)

    # 1. Open a goal
    temp_ledger.append(
        kind="goal_open",
        content=json.dumps({"text": "Fix bugs", "goal_id": "g1"})
    )
    mirror.sync()

    assert "g1" in mirror.open_goals
    assert mirror.open_goals["g1"]["status"] == "OPEN"
    assert mirror.open_goals["g1"]["text"] == "Fix bugs"

    # 2. Close the goal
    temp_ledger.append(
        kind="goal_close",
        content=json.dumps({"goal_id": "g1", "reason": "Done"})
    )
    mirror.sync()

    assert "g1" not in mirror.open_goals
    assert "g1" in mirror.closed_goals
    assert mirror.closed_goals["g1"]["status"] == "CLOSED"
    assert mirror.closed_goals["g1"]["close_reason"] == "Done"


def test_determinism_rebuild(temp_ledger):
    """Test that rebuild produces same state as incremental sync."""
    mirror1 = SparringMirror(temp_ledger)
    
    # Create a history of events
    temp_ledger.append(kind="session_start", content=json.dumps({"domain": "writer"}))
    temp_ledger.append(kind="goal_open", content=json.dumps({"text": "Write ch1", "goal_id": "g1"}))
    temp_ledger.append(kind="reflection", content="{}")
    temp_ledger.append(kind="goal_close", content=json.dumps({"goal_id": "g1"}))
    temp_ledger.append(kind="goal_open", content=json.dumps({"text": "Write ch2", "goal_id": "g2"}))

    # Sync mirror1 incrementally
    mirror1.sync()
    
    # Create mirror2 and rebuild from scratch
    mirror2 = SparringMirror(temp_ledger)
    mirror2.rebuild()
    
    # Validate identical state
    assert mirror1.current_domain == mirror2.current_domain
    assert mirror1.open_goals == mirror2.open_goals
    assert mirror1.closed_goals == mirror2.closed_goals
    assert mirror1.reflection_counts == mirror2.reflection_counts
    assert mirror1.last_event_id == mirror2.last_event_id


def test_domain_tracking(temp_ledger):
    """Test domain switching logic."""
    mirror = SparringMirror(temp_ledger)
    
    temp_ledger.append(kind="session_start", content=json.dumps({"domain": "business"}))
    mirror.sync()
    assert mirror.current_domain == "business"
    
    temp_ledger.append(kind="domain_change", content=json.dumps({"domain": "personal"}))
    mirror.sync()
    assert mirror.current_domain == "personal"
    
    assert len(mirror.domain_history) == 1
    assert mirror.domain_history[0]["domain"] == "personal"


def test_abandoned_goals(temp_ledger):
    """Test goal abandonment."""
    mirror = SparringMirror(temp_ledger)
    
    temp_ledger.append(kind="goal_open", content=json.dumps({"goal_id": "g_fail"}))
    mirror.sync()
    
    temp_ledger.append(kind="goal_abandon", content=json.dumps({"goal_id": "g_fail", "reason": "Too hard"}))
    mirror.sync()
    
    assert "g_fail" not in mirror.open_goals
    assert "g_fail" in mirror.closed_goals
    assert mirror.closed_goals["g_fail"]["status"] == "ABANDONED"


