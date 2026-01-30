"""Tests for the Recursive Self-Model (RSM)."""

import json
import os
import tempfile
import pytest

from lib.ledger import SparringLedger
from lib.mirror import SparringMirror
from lib.rsm import SparringRSM


@pytest.fixture
def temp_env():
    """Create a temporary ledger and mirror for testing."""
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    ledger = SparringLedger(path)
    mirror = SparringMirror(ledger)
    yield ledger, mirror
    ledger.close()
    os.unlink(path)


def test_rsm_init(temp_env):
    """Test RSM initialization."""
    ledger, mirror = temp_env
    rsm = SparringRSM(mirror)
    assert rsm.tendencies == {}
    assert rsm.metrics == {}


def test_detect_high_performer(temp_env):
    """Test detection of high performer tendency."""
    ledger, mirror = temp_env
    rsm = SparringRSM(mirror)

    # 1. Create 6 closed goals (total > 5, rate 100%)
    for i in range(6):
        ledger.append(kind="goal_open", content=json.dumps({"goal_id": f"g{i}"}))
        ledger.append(kind="goal_close", content=json.dumps({"goal_id": f"g{i}"}))
    
    mirror.sync()
    rsm.analyze()

    assert rsm.metrics["total_goals"] == 6
    assert rsm.metrics["completion_rate"] == 1.0
    assert rsm.tendencies.get("high_performer") is True


def test_detect_struggle_prone(temp_env):
    """Test detection of struggle prone tendency."""
    ledger, mirror = temp_env
    rsm = SparringRSM(mirror)

    # 2 abandoned, 1 closed
    ledger.append(kind="goal_open", content=json.dumps({"goal_id": "g1"}))
    ledger.append(kind="goal_abandon", content=json.dumps({"goal_id": "g1"}))
    
    ledger.append(kind="goal_open", content=json.dumps({"goal_id": "g2"}))
    ledger.append(kind="goal_abandon", content=json.dumps({"goal_id": "g2"}))
    
    ledger.append(kind="goal_open", content=json.dumps({"goal_id": "g3"}))
    ledger.append(kind="goal_close", content=json.dumps({"goal_id": "g3"}))

    mirror.sync()
    rsm.analyze()

    assert rsm.metrics["abandoned_count"] == 2
    assert rsm.tendencies.get("struggle_prone") is True


def test_completion_momentum(temp_env):
    """Test detection of 3 consecutive completions."""
    ledger, mirror = temp_env
    rsm = SparringRSM(mirror)

    # 3 consecutive closes
    ledger.append(kind="goal_close", content=json.dumps({"goal_id": "g1"}))
    ledger.append(kind="goal_close", content=json.dumps({"goal_id": "g2"}))
    ledger.append(kind="goal_close", content=json.dumps({"goal_id": "g3"}))

    mirror.sync()
    rsm.analyze()

    assert rsm.tendencies.get("completion_momentum") is True

    # Break momentum
    ledger.append(kind="goal_open", content=json.dumps({"goal_id": "g4"}))
    
    mirror.sync()
    rsm.analyze()
    
    assert rsm.tendencies.get("completion_momentum") is False


def test_publish_snapshot(temp_env):
    """Test emitting an RSM snapshot to the ledger."""
    ledger, mirror = temp_env
    rsm = SparringRSM(mirror)
    
    # 1. Create some state
    ledger.append(kind="goal_open", content=json.dumps({"goal_id": "g1"}))
    mirror.sync()
    
    # 2. Publish snapshot
    event_id = rsm.publish_snapshot()
    assert event_id > 0
    
    # 3. Verify event
    evt = ledger.get(event_id)
    assert evt["kind"] == "rsm_snapshot"
    data = json.loads(evt["content"])
    assert "tendencies" in data
    assert "metrics" in data

