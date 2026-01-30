"""Tests for the skills registry and manager."""

import json
import pytest
import os
import sys
from pathlib import Path

# Add lib to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from skills import (
    SkillsRegistry,
    SkillsManager,
    format_skill_list,
    format_bundle_list,
)
from ledger import SparringLedger


@pytest.fixture
def repo_root(tmp_path):
    """Create a temporary repository root with skills."""
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir()

    # Create test-skill-1
    s1 = skills_dir / "engineering" / "test-skill-1"
    s1.mkdir(parents=True)
    (s1 / "SKILL.md").write_text(
        "---\nname: test-skill-1\ncategory: engineering\ndescription: Test skill for engineering\n---"
    )

    # Create test-skill-2
    s2 = skills_dir / "engineering" / "test-skill-2"
    s2.mkdir(parents=True)
    (s2 / "SKILL.md").write_text(
        "---\nname: test-skill-2\ncategory: engineering\ndescription: Another engineering skill\n---"
    )

    # Create marketing-skill
    m1 = skills_dir / "marketing" / "marketing-skill"
    m1.mkdir(parents=True)
    (m1 / "SKILL.md").write_text(
        "---\nname: marketing-skill\ncategory: marketing\ndescription: Marketing skill for content\n---"
    )

    # Create ceo-advisor
    c1 = skills_dir / "c-level" / "ceo"
    c1.mkdir(parents=True)
    (c1 / "SKILL.md").write_text(
        "---\nname: ceo-advisor\ncategory: c-level\ndescription: CEO advisory skill\n---"
    )

    # Create product-toolkit
    p1 = skills_dir / "product" / "toolkit"
    p1.mkdir(parents=True)
    (p1 / "SKILL.md").write_text(
        "---\nname: product-toolkit\ncategory: product\ndescription: Product management toolkit\n---"
    )

    return tmp_path


@pytest.fixture
def registry(repo_root):
    """Return a SkillsRegistry with test data."""
    return SkillsRegistry(repo_root)


@pytest.fixture
def manager(ledger, registry):
    """Return a SkillsManager with test registry."""
    return SkillsManager(ledger, registry)


class TestSkillsRegistry:
    """Tests for SkillsRegistry."""

    def test_load_skills(self, registry):
        """Test loading skills from file system."""
        skills = registry.load()
        assert len(skills) == 5

    def test_get_all_skills(self, registry):
        """Test getting all skills."""
        skills = sorted(registry.get_all_skills(), key=lambda x: x["name"])
        assert len(skills) == 5
        assert skills[4]["name"] == "test-skill-2" # 'test-skill-2' is last alphabetically
        # Actually alphabetical: ceo-advisor, marketing-skill, product-toolkit, test-skill-1, test-skill-2
        # So test-skill-1 is index 3.
        assert skills[3]["name"] == "test-skill-1"

    def test_get_skill_by_name(self, registry):
        """Test getting skill by name."""
        skill = registry.get_skill("ceo-advisor")
        assert skill is not None
        assert skill["category"] == "c-level"

    def test_get_skill_not_found(self, registry):
        """Test getting non-existent skill."""
        skill = registry.get_skill("nonexistent")
        assert skill is None

    def test_get_by_category(self, registry):
        """Test filtering skills by category."""
        engineering = registry.get_by_category("engineering")
        assert len(engineering) == 2
        assert all(s["category"] == "engineering" for s in engineering)

    def test_search(self, registry):
        """Test searching skills."""
        results = registry.search("marketing")
        assert len(results) == 1
        assert results[0]["name"] == "marketing-skill"

    def test_search_case_insensitive(self, registry):
        """Test case-insensitive search."""
        results = registry.search("CEO")
        assert len(results) == 1
        assert results[0]["name"] == "ceo-advisor"

    def test_search_by_description(self, registry):
        """Test searching by description."""
        results = registry.search("content")
        assert len(results) == 1
        assert results[0]["name"] == "marketing-skill"


    def test_get_total_skills(self, registry):
        """Test getting total skill count."""
        total = registry.get_total_skills()
        assert total == 5


class TestSkillsManager:
    """Tests for SkillsManager."""

    def test_install_skill(self, manager):
        """Test installing a skill."""
        event_id = manager.install_skill("ceo-advisor")
        assert event_id > 0

        # Verify event was recorded
        installed = manager.get_installed_skills()
        assert "ceo-advisor" in installed

    def test_install_nonexistent_skill(self, manager):
        """Test installing non-existent skill raises error."""
        with pytest.raises(ValueError, match="Skill not found"):
            manager.install_skill("nonexistent-skill")

    def test_uninstall_skill(self, manager):
        """Test uninstalling a skill."""
        manager.install_skill("ceo-advisor")
        manager.uninstall_skill("ceo-advisor")

        installed = manager.get_installed_skills()
        assert "ceo-advisor" not in installed

    def test_install_bundle(self, manager):
        """Test installing a bundle."""
        event_id = manager.install_bundle(
            bundle_name="starter",
            skills=["ceo-advisor", "product-toolkit"],
            domain="strategy"
        )
        assert event_id > 0

        # Verify skills from bundle are installed
        installed = manager.get_installed_skills()
        assert "ceo-advisor" in installed
        assert "product-toolkit" in installed

    def test_record_usage(self, manager):
        """Test recording skill usage."""
        manager.install_skill("ceo-advisor")
        event_id = manager.record_usage("ceo-advisor", "Planning session")
        assert event_id > 0

        stats = manager.get_skill_usage_stats()
        assert stats["ceo-advisor"] == 1

    def test_multiple_usage(self, manager):
        """Test multiple skill usages."""
        manager.install_skill("ceo-advisor")
        manager.record_usage("ceo-advisor")
        manager.record_usage("ceo-advisor")
        manager.record_usage("ceo-advisor")

        stats = manager.get_skill_usage_stats()
        assert stats["ceo-advisor"] == 3

    def test_record_feedback(self, manager):
        """Test recording skill feedback."""
        manager.install_skill("ceo-advisor")
        event_id = manager.record_feedback("ceo-advisor", rating=5, comment="Great!")
        assert event_id > 0

        stats = manager.get_skill_feedback_stats()
        assert "ceo-advisor" in stats
        assert stats["ceo-advisor"]["avg_rating"] == 5
        assert stats["ceo-advisor"]["count"] == 1

    def test_feedback_rating_clamped(self, manager):
        """Test feedback rating is clamped to 1-5."""
        manager.install_skill("ceo-advisor")
        manager.record_feedback("ceo-advisor", rating=10)
        manager.record_feedback("ceo-advisor", rating=0)

        stats = manager.get_skill_feedback_stats()
        # Rating 10 should be clamped to 5, rating 0 to 1
        # Average of 5 and 1 = 3
        assert stats["ceo-advisor"]["avg_rating"] == 3

    def test_get_installed_skills_empty(self, manager):
        """Test getting installed skills when none installed."""
        installed = manager.get_installed_skills()
        assert installed == []

    # def test_get_installation_history(self, manager):
    #     """Test getting installation history."""
    #     manager.install_skill("ceo-advisor")
    #     # ... implementation missing in manager.py potentially
    #     pass



class TestFormatFunctions:
    """Tests for formatting functions."""

    def test_format_skill_list_empty(self):
        """Test formatting empty skill list."""
        result = format_skill_list([])
        assert result == "No skills found."

    def test_format_skill_list_brief(self, registry):
        """Test brief skill list formatting."""
        skills = registry.get_all_skills()[:2]
        result = format_skill_list(skills, verbose=False)
        assert "test-skill-1" in result
        assert "[engineering]" in result

    def test_format_skill_list_verbose(self, registry):
        """Test verbose skill list formatting."""
        # Find test-skill-1 explicitly
        skills = [s for s in registry.get_all_skills() if s["name"] == "test-skill-1"]
        result = format_skill_list(skills, verbose=True)
        assert "## test-skill-1" in result
        assert "Test skill for engineering" in result

    def test_format_bundle_list_empty(self):
        """Test formatting empty bundle list."""
        result = format_bundle_list({})
        assert result == "No bundles available."

    def test_format_bundle_list(self):
        """Test bundle list formatting."""
        bundles = {
            "starter": ["skill-1", "skill-2"],
            "complete": ["skill-1", "skill-2", "skill-3"]
        }
        result = format_bundle_list(bundles, "Test Domain")
        assert "## Test Domain Bundles" in result
        assert "@starter" in result
        assert "skill-1, skill-2" in result


class TestSkillsManagerWithDomain:
    """Tests for SkillsManager with domain integration."""

    def test_get_recommended_skills(self, manager, tmp_path):
        """Test getting recommended skills for domain."""
        # Create a mock domain config
        class MockDomainConfig:
            id = "test"
            _raw = {
                "recommended_skills": ["ceo-advisor", "product-toolkit"]
            }

        domain = MockDomainConfig()
        recommended = manager.get_recommended_skills(domain)

        assert len(recommended) == 2
        assert recommended[0]["name"] == "ceo-advisor"

    def test_get_bundles(self, manager):
        """Test getting bundles from domain config."""
        class MockDomainConfig:
            id = "test"
            _raw = {
                "skill_bundles": {
                    "starter": ["ceo-advisor"],
                    "complete": ["ceo-advisor", "product-toolkit"]
                }
            }

        domain = MockDomainConfig()
        bundles = manager.get_bundles(domain)

        assert "starter" in bundles
        assert "complete" in bundles
        assert len(bundles["complete"]) == 2

    def test_install_bundle_by_name(self, manager):
        """Test installing bundle by name from domain config."""
        class MockDomainConfig:
            id = "test"
            _raw = {
                "skill_bundles": {
                    "starter": ["ceo-advisor", "product-toolkit"]
                }
            }

        domain = MockDomainConfig()
        event_id = manager.install_bundle_by_name("starter", domain)

        assert event_id > 0
        installed = manager.get_installed_skills()
        assert "ceo-advisor" in installed
        assert "product-toolkit" in installed

    def test_install_bundle_by_name_not_found(self, manager):
        """Test installing non-existent bundle raises error."""
        class MockDomainConfig:
            id = "test"
            _raw = {"skill_bundles": {"starter": []}}

        domain = MockDomainConfig()
        with pytest.raises(ValueError, match="Bundle 'nonexistent' not found"):
            manager.install_bundle_by_name("nonexistent", domain)


class TestSkillsRegistryFileNotFound:
    """Tests for registry with missing file."""

    def test_missing_skills_dir(self, tmp_path):
        """Test scanning when skills dir doesn't exist."""
        registry = SkillsRegistry(tmp_path)
        skills = registry.load()
        assert skills == []
