#!/usr/bin/env python3
"""Quick verification script for Conversational Sparring system.

Runs all diagnostic tests and generates a summary report.
"""

import sys
from pathlib import Path

# Add lib to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.ledger import SparringLedger
from lib.domains import load_domain, list_available_domains, get_default_domain


def test_ledger():
    """Test ledger integrity."""
    print("\n=== LEDGER TEST ===")
    ledger = SparringLedger()

    try:
        is_valid = ledger.verify_chain()
        print(f"Hash Chain: {'✓ VALID' if is_valid else '✗ INVALID'}")
    except Exception as e:
        print(f"✗ Hash Chain Error: {e}")
        return False

    all_events = ledger.read_all()
    print(f"Total events: {len(all_events)}")

    # Event counts
    event_types = [
        'session_start', 'goal_open', 'goal_close', 'skill_use',
        'pattern_detected', 'cognitive_mode_switch', 'domain_change'
    ]

    for kind in event_types:
        events = ledger.read_by_kind(kind)
        status = "✓" if len(events) > 0 else "✗"
        print(f"  {status} {kind}: {len(events)}")

    return True


def test_domains():
    """Test domain system."""
    print("\n=== DOMAIN SYSTEM TEST ===")

    available = list_available_domains()
    print(f"Available domains: {len(available)}")
    print(f"  {', '.join(available)}")

    default = get_default_domain()
    print(f"\nDefault domain: {default}")

    if default not in available:
        print(f"  ✗ CRITICAL: Default domain '{default}' does not exist!")
        return False
    else:
        print(f"  ✓ Default domain exists")

    # Test strategic-research
    try:
        domain = load_domain('strategic-research')
        print(f"\nstrategic-research domain:")
        print(f"  Name: {domain.name}")
        print(f"  Patterns: {len(domain.patterns)}")
        print(f"  Categories: {len(domain.categories)}")

        if len(domain.categories) == 0:
            print(f"  ✗ HIGH: No categories defined!")
            return False
        else:
            print(f"  ✓ Categories defined")

        # Test category detection
        test_desc = "Research how Gen Z uses video and reels for global insight consumption"
        category = domain.detect_category(test_desc)
        impact = domain.calculate_impact_score(test_desc)

        print(f"\nCategory Detection Test:")
        print(f"  Description: {test_desc[:60]}...")
        print(f"  Detected category: {category}")
        print(f"  Impact score: {impact}/10")

        if category == "other" or impact < 6:
            print(f"  ✗ Category detection suboptimal")
            return False
        else:
            print(f"  ✓ Category detection working")

    except Exception as e:
        print(f"✗ Error loading strategic-research: {e}")
        return False

    return True


def test_cognitive_router():
    """Test cognitive router."""
    print("\n=== COGNITIVE ROUTER TEST ===")

    try:
        from lib.cognition import CognitiveRouter
        from lib.ledger import SparringLedger

        ledger = SparringLedger()
        router = CognitiveRouter(ledger)

        query = "I want to research how Gen Z uses video and reels"
        mode, confidence = router.determine_mode(query)

        print(f"Query: {query[:60]}...")
        print(f"Detected mode: {mode}")
        print(f"Confidence: {confidence:.2f}")

        ere_level = router.get_current_ere_level()
        print(f"ERE Level: {ere_level.value} ({ere_level.name})")

        # Check if event was created
        cognitive_events = ledger.read_by_kind('cognitive_mode_switch')
        if len(cognitive_events) == 0:
            print(f"✗ No cognitive_mode_switch events (not integrated)")
            return False
        else:
            print(f"✓ Cognitive mode switch tracked")

    except Exception as e:
        print(f"✗ Error: {e}")
        return False

    return True


def test_autonomy():
    """Test autonomy kernel."""
    print("\n=== AUTONOMY KERNEL TEST ===")

    try:
        from lib.autonomy import SparringAutonomy
        from lib.rsm import SparringRSM
        from lib.ledger import SparringLedger

        ledger = SparringLedger()
        rsm = SparringRSM(ledger)
        autonomy = SparringAutonomy(ledger, rsm)

        decision = autonomy.decide_next_action()

        print(f"Next action: {decision.get('action', 'N/A')}")
        print(f"Reason: {decision.get('reason', 'N/A')}")

        if 'action' not in decision:
            print(f"✗ Decision incomplete")
            return False
        else:
            print(f"✓ Autonomy working")

    except Exception as e:
        print(f"✗ Error: {e}")
        return False

    return True


def main():
    """Run all tests."""
    print("=" * 60)
    print("CONVERSATIONAL SPARRING SYSTEM VERIFICATION")
    print("=" * 60)

    tests = [
        ("Ledger", test_ledger),
        ("Domain System", test_domains),
        ("Cognitive Router", test_cognitive_router),
        ("Autonomy Kernel", test_autonomy),
    ]

    results = {}
    for name, test_func in tests:
        try:
            results[name] = test_func()
        except Exception as e:
            print(f"\n✗ {name} CRASHED: {e}")
            results[name] = False

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for name, passed_test in results.items():
        status = "✓ PASS" if passed_test else "✗ FAIL"
        print(f"{status:10s} {name}")

    print(f"\nTotal: {passed}/{total} tests passed ({passed/total*100:.0f}%)")

    if passed < total:
        print("\nSee reports/diagnostic_report.md for detailed analysis and fixes.")
        sys.exit(1)
    else:
        print("\n✓ All systems operational!")
        sys.exit(0)


if __name__ == "__main__":
    main()
