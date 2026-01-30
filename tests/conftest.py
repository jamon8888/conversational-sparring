
import pytest
import os
import sys

# Add lib to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from ledger import SparringLedger

@pytest.fixture
def ledger():
    """Return a fresh in-memory ledger."""
    return SparringLedger(":memory:")

@pytest.fixture
def temp_ledger(tmp_path):
    """Return a ledger backed by a temporary file."""
    db_path = tmp_path / "sparring.db"
    return SparringLedger(str(db_path))
