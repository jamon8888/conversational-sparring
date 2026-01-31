
import pytest
from domains import load_domain, list_available_domains, get_default_domain, domain_exists

class TestDomainSystem:
    """Test the domain configuration system."""

    def test_domain_loader_structure(self):
        """Test that domain module functions exist."""
        assert callable(load_domain)
        assert callable(list_available_domains)
        assert callable(get_default_domain)

    def test_default_domain_is_personal(self):
        """Test default domain is personal."""
        assert get_default_domain() == "personal"

    def test_load_builtin_domain_c_level(self):
        """Test loading the built-in c-level domain."""
        try:
            config = load_domain("c-level")
            assert config.id == "c-level"
            assert "CEO" in config.description or "C-Level" in config.name or "Executive" in config.description
        except ImportError:
            pytest.skip("PyYAML not installed")

    def test_invalid_domain_raises_error(self):
        """Test that loading a non-existent domain raises ValueError."""
        try:
            with pytest.raises(ValueError):
                load_domain("non_existent_domain_xyz")
        except ImportError:
            pytest.skip("PyYAML not installed")

    def test_domain_exists_check(self):
        """Test domain_exists utility."""
        assert domain_exists("personal") is True
        assert domain_exists("c-level") is True
        assert domain_exists("completely_fake_domain") is False

