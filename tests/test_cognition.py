
import pytest
import json
from cognition import CognitiveRouter, CognitiveMode, ERELevel
from ledger import SparringLedger

class TestCognition:
    """Test the cognitive logic."""

    def test_router_decision_mode(self, ledger):
        """Test detection of decision mode."""
        router = CognitiveRouter(ledger)
        
        mode, conf = router.determine_mode("Should I migrate to Next.js?")
        assert mode == CognitiveMode.DECISION
        assert conf > 0.5

    def test_router_learning_mode(self, ledger):
        """Test detection of learning mode."""
        router = CognitiveRouter(ledger)
        
        mode, conf = router.determine_mode("How do I start with React?")
        assert mode == CognitiveMode.LEARNING
        assert conf > 0.5
        
    def test_router_ambiguous_fallback(self, ledger):
        """Test fallback for ambiguous input."""
        router = CognitiveRouter(ledger)
        
        mode, conf = router.determine_mode("Hello there")
        # Should lean learning or default
        assert mode == CognitiveMode.LEARNING

    def test_ere_level_calculation(self, ledger):
        """Test ERE level progression."""
        router = CognitiveRouter(ledger)
        
        # New user = Novice
        assert router.get_current_ere_level() == ERELevel.NOVICE
        
        # Simulate experience
        for i in range(15):
             ledger.append(kind="goal_close", content='{"outcome": "success"}')
             
        # >10 completions = Advanced
        assert router.get_current_ere_level() == ERELevel.ADVANCED
        
    def test_state_recording(self, ledger):
        """Test recording of cognitive events."""
        router = CognitiveRouter(ledger)
        
        router.record_switch(CognitiveMode.DECISION, "User asked for advice")
        
        events = ledger.read_by_kind("cognitive_mode_switch")
        assert len(events) == 1
        assert json.loads(events[0]["content"])["mode"] == "decision"
