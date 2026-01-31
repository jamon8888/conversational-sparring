import pytest
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.ledger import SparringLedger
from lib.goals import GoalManager
from lib.domains.loader import load_domain, list_available_domains

def test_csuite_domains_exist():
    """Verify core C-Suite style domains are available."""
    domains = list_available_domains()
    # Updated to match actual domain files
    expected_domains = {
        "c-level",        # CEO/Executive (was strategy)
        "engineering", 
        "marketing-growth",  # Growth (was growth)
        "product",
        "sales",
        "operations",
        "people"
    }
    
    # Check if all expected are present
    missing = expected_domains - set(domains)
    assert not missing, f"Missing C-Suite domains: {missing}"
    
    # Verify legacy ones are gone
    assert "developer" not in domains, "Legacy 'developer' domain should be gone"
    assert "business" not in domains, "Legacy 'business' domain should be gone"
    assert "strategy" not in domains, "Legacy 'strategy' domain renamed to c-level"
    assert "growth" not in domains, "Legacy 'growth' domain renamed to marketing-growth"

def test_solofounder_workflow():
    """Simulate a Solofounder moving through the C-Suite."""
    
    ledger = SparringLedger(":memory:") # Use in-memory DB
    goals = GoalManager(ledger)
    
    # 1. CEO (C-Level): Set Vision
    clevel_config = load_domain("c-level")
    assert clevel_config.id == "c-level"
    goals._domain = clevel_config  # Set domain before creating goal
    
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
    assert "c-level" in domains_in_play
    assert "product" in domains_in_play
    assert "engineering" in domains_in_play

def test_domain_content_migration():
    """Verify content migrated correctly (e.g. keywords)."""
    
    # Marketing-growth should have acquisition keywords
    marketing_growth = load_domain("marketing-growth")
    categories = marketing_growth.get_valid_categories()
    assert len(categories) > 0, "marketing-growth should have categories"
    
    # Engineering should have CTO focus but retain tech keywords
    eng = load_domain("engineering")
    eng_categories = eng.get_valid_categories()
    assert len(eng_categories) > 0, "engineering should have categories"
    
    # C-level should have executive focus
    clevel = load_domain("c-level")
    clevel_categories = clevel.get_valid_categories()
    assert len(clevel_categories) > 0, "c-level should have categories"
