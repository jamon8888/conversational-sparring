import pytest
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.ledger import SparringLedger
from lib.goals import GoalManager
from lib.domains.loader import load_domain, list_available_domains

def test_csuite_domains_exist():
    """Verify all 7 C-Suite domains are available."""
    domains = list_available_domains()
    expected_domains = {
        "strategy",
        "engineering", 
        "growth",
        "product",
        "sales",
        "operations",
        "people"
    }
    
    # Check if all expected are present
    missing = expected_domains - set(domains)
    assert not missing, f"Missing C-Suite domains: {missing}"
    
    # Verify legacy ones are gone (optional, but good hygiene)
    assert "developer" not in domains, "Legacy 'developer' domain should be gone"
    assert "business" not in domains, "Legacy 'business' domain should be gone"

def test_solofounder_workflow():
    """Simulate a Solofounder moving through the C-Suite."""
    
    ledger = SparringLedger(":memory:") # Use in-memory DB
    goals = GoalManager(ledger)
    
    # 1. CEO (Strategy): Set Vision
    strategy_config = load_domain("strategy")
    assert strategy_config.id == "strategy"
    
    goal_id_1 = goals.open_goal(
        description="Define 2026 Vision",
        category="planning"
    )
    assert goal_id_1 is not None
    
    # 2. CPO (Product): Define MVP
    product_config = load_domain("product")
    goals._domain = product_config # Simulate domain switch
    
    goal_id_2 = goals.open_goal(
        description="Spec out MVP for mobile app",
        category="roadmap"
    )
    
    # 3. CTO (Engineering): Build it
    eng_config = load_domain("engineering")
    goals._domain = eng_config # Simulate domain switch
    
    goal_id_3 = goals.open_goal(
        description="Initialize React Native repo",
        category="devops"  # assuming devops is a category in new engineering
    )
    
    # Verify we can read them back
    active_goals = goals.get_open_goals()
    assert len(active_goals) == 3
    
    domains_in_play = {g.get("domain") for g in active_goals}
    assert "strategy" in domains_in_play
    assert "product" in domains_in_play
    assert "engineering" in domains_in_play

def test_domain_content_migration():
    """Verify content migrated correctly (e.g. keywords)."""
    
    # Growth should have marketing keywords
    growth = load_domain("growth")
    assert "acquisition" in growth.get_valid_categories()
    
    # Engineering should have CTO focus but retain tech keywords
    eng = load_domain("engineering")
    assert "design" in eng.get_valid_categories() # from legacy engineering/developer
    
    # Strategy should have CEO focus
    strat = load_domain("strategy")
    assert "initiative" in strat.get_valid_categories()

