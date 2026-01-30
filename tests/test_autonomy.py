"""Tests for the Autonomy Kernel."""

import json
import os
import tempfile
from datetime import datetime, timedelta, timezone
import pytest

from lib.ledger import SparringLedger
from lib.mirror import SparringMirror
from lib.rsm import SparringRSM
from lib.autonomy import SparringAutonomy


@pytest.fixture
def temp_env():
    """Create a temporary testing environment."""
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    ledger = SparringLedger(path)
    mirror = SparringMirror(ledger)
    rsm = SparringRSM(mirror)
    autonomy = SparringAutonomy(mirror, rsm)
    yield ledger, mirror, rsm, autonomy
    ledger.close()
    os.unlink(path)


def test_autonomy_idle(temp_env):
    """Test that no action is taken when state is clean."""
    ledger, mirror, rsm, autonomy = temp_env
    
    # Just one open goal, recently created
    ledger.append(kind="goal_open", content=json.dumps({"goal_id": "g1"}))
    
    decision = autonomy.decide_next_action()
    assert decision.action == "idle"


def test_autonomy_intervene(temp_env):
    """Test that struggle triggers intervention."""
    ledger, mirror, rsm, autonomy = temp_env
    
    # Create struggle condition (more abandoned than closed)
    ledger.append(kind="goal_open", content=json.dumps({"goal_id": "g1"}))
    ledger.append(kind="goal_abandon", content=json.dumps({"goal_id": "g1"}))
    ledger.append(kind="goal_open", content=json.dumps({"goal_id": "g2"}))
    ledger.append(kind="goal_abandon", content=json.dumps({"goal_id": "g2"}))
    
    # Ensure RSM detects it
    mirror.sync()
    rsm.analyze()
    assert rsm.tendencies.get("struggle_prone") is True
    
    decision = autonomy.decide_next_action()
    assert decision.action == "intervene"
    assert "struggle_prone_tendency" in decision.evidence


def test_autonomy_reflect(temp_env):
    """Test reflection prompt after 5 completions."""
    ledger, mirror, rsm, autonomy = temp_env
    
    # Close 6 goals
    for i in range(6):
        ledger.append(kind="goal_open", content=json.dumps({"goal_id": f"g{i}"}))
        ledger.append(kind="goal_close", content=json.dumps({"goal_id": f"g{i}"}))
        
    decision = autonomy.decide_next_action()
    assert decision.action == "reflect"


def test_autonomy_stalled(temp_env):
    """Test check-in for stalled goals."""
    ledger, mirror, rsm, autonomy = temp_env
    
    # Inject an old goal event using manual timestamp override if possible, 
    # but the ledger automatically timestamps. 
    # Instead, we'll patch datetime in autonomy module or mock, 
    # OR we can just insert a raw SQL row with old timestamp since we have the ledger connection.
    
    # Let's insert via SQL to fake the timestamp
    with ledger._conn:
        stale_ts = (datetime.now(timezone.utc) - timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        content = json.dumps({"goal_id": "stale_1", "text": "Old goal"})
        ledger._conn.execute(
            "INSERT INTO events (ts, kind, content, meta, hash) VALUES (?, ?, ?, ?, ?)",
            (stale_ts, "goal_open", content, "{}", "fake_hash")
        )

    # Force sync (mirror relies on internal counters, but read_since uses ID)
    # Since we inserted manually without updating AUTOINCREMENT normally, let's just 
    # ensure mirror reads it.
    
    # Actually, simpler to just lower the threshold for the test instance
    autonomy.thresholds["stalled_goal_days"] = 0  # Immediate stall
    
    ledger.append(kind="goal_open", content=json.dumps({"goal_id": "g_stalled"}))
    
    decision = autonomy.decide_next_action()
    assert decision.action == "check_in"
    assert "g_stalled" in decision.evidence

