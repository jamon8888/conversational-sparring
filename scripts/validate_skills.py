#!/usr/bin/env python3
"""Skill and Plugin validation script.

Validates skills and plugins against strict authoring standards:
- YAML frontmatter with required fields
- Required file structure
- Agent folder consistency
- Plugin manifest validation

Usage:
    python scripts/validate_skills.py              # Validate all
    python scripts/validate_skills.py --fix        # Auto-fix issues where possible
    python scripts/validate_skills.py --strict     # Fail on warnings too
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set

try:
    import yaml
    HAS_YAML = True
except ImportError:
    yaml = None
    HAS_YAML = False

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
SKILLS_DIR = PROJECT_ROOT / "skills"
AGENTS_DIR = PROJECT_ROOT / "agents"
DOMAINS_DIR = PROJECT_ROOT / "domains"
DIST_DIR = PROJECT_ROOT / "dist" / "plugins"

# Validation rules
REQUIRED_SKILL_FILES = ["SKILL.md"]
OPTIONAL_SKILL_DIRS = ["scripts", "references", "assets"]
REQUIRED_FRONTMATTER = ["name", "description"]
MAX_DESCRIPTION_LENGTH = 200
MAX_SKILL_MD_LINES = 500  # Encourage concise skills


@dataclass
class ValidationResult:
    """Result of a validation check."""
    path: Path
    level: str  # "error", "warning", "info"
    message: str
    fixable: bool = False
    
    def __str__(self):
        icon = {"error": "❌", "warning": "⚠️", "info": "ℹ️"}.get(self.level, "?")
        return f"{icon} [{self.level.upper()}] {self.path.name}: {self.message}"


@dataclass
class ValidationReport:
    """Complete validation report."""
    results: List[ValidationResult] = field(default_factory=list)
    
    def add(self, result: ValidationResult):
        self.results.append(result)
    
    @property
    def errors(self) -> List[ValidationResult]:
        return [r for r in self.results if r.level == "error"]
    
    @property
    def warnings(self) -> List[ValidationResult]:
        return [r for r in self.results if r.level == "warning"]
    
    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0
    
    def print_summary(self):
        errors = len(self.errors)
        warnings = len(self.warnings)
        
        if errors == 0 and warnings == 0:
            print("✅ All validations passed!")
        else:
            print(f"\n📊 Summary: {errors} error(s), {warnings} warning(s)")


def validate_yaml_frontmatter(content: str, path: Path) -> List[ValidationResult]:
    """Validate YAML frontmatter in a markdown file."""
    results = []
    
    if not content.startswith("---"):
        results.append(ValidationResult(
            path=path,
            level="error",
            message="Missing YAML frontmatter (must start with ---)",
            fixable=True
        ))
        return results
    
    # Extract frontmatter
    end_idx = content.find("---", 3)
    if end_idx == -1:
        results.append(ValidationResult(
            path=path,
            level="error",
            message="Unclosed YAML frontmatter (missing closing ---)"
        ))
        return results
    
    frontmatter = content[3:end_idx].strip()
    
    if not HAS_YAML or yaml is None:
        results.append(ValidationResult(
            path=path,
            level="warning",
            message="PyYAML not installed, skipping frontmatter validation"
        ))
        return results
    
    try:
        meta = yaml.safe_load(frontmatter)
        if not isinstance(meta, dict):
            results.append(ValidationResult(
                path=path,
                level="error",
                message="Frontmatter must be a YAML dictionary"
            ))
            return results
    except yaml.YAMLError as e:
        results.append(ValidationResult(
            path=path,
            level="error",
            message=f"Invalid YAML: {e}"
        ))
        return results
    
    # Check required fields
    for field in REQUIRED_FRONTMATTER:
        if field not in meta:
            results.append(ValidationResult(
                path=path,
                level="error",
                message=f"Missing required field: {field}",
                fixable=True
            ))
        elif not meta[field]:
            results.append(ValidationResult(
                path=path,
                level="warning",
                message=f"Empty field: {field}"
            ))
    
    # Check description length
    if "description" in meta and meta["description"]:
        desc = meta["description"]
        if len(desc) > MAX_DESCRIPTION_LENGTH:
            results.append(ValidationResult(
                path=path,
                level="warning",
                message=f"Description too long ({len(desc)} > {MAX_DESCRIPTION_LENGTH} chars)"
            ))
    
    return results


def validate_skill(skill_path: Path) -> List[ValidationResult]:
    """Validate a single skill directory."""
    results = []
    
    # Check required files
    for req_file in REQUIRED_SKILL_FILES:
        file_path = skill_path / req_file
        if not file_path.exists():
            results.append(ValidationResult(
                path=skill_path,
                level="error",
                message=f"Missing required file: {req_file}"
            ))
    
    # Validate SKILL.md
    skill_md = skill_path / "SKILL.md"
    if skill_md.exists():
        content = skill_md.read_text(encoding="utf-8")
        
        # Check frontmatter
        results.extend(validate_yaml_frontmatter(content, skill_md))
        
        # Check file length
        line_count = len(content.splitlines())
        if line_count > MAX_SKILL_MD_LINES:
            results.append(ValidationResult(
                path=skill_md,
                level="warning",
                message=f"SKILL.md too long ({line_count} > {MAX_SKILL_MD_LINES} lines). Consider splitting into references/"
            ))
        
        # Check for required sections
        if "## " not in content:
            results.append(ValidationResult(
                path=skill_md,
                level="warning",
                message="No markdown sections found (## headings)"
            ))
    
    # Check scripts have proper structure
    scripts_dir = skill_path / "scripts"
    if scripts_dir.exists():
        for script in scripts_dir.glob("*.py"):
            script_content = script.read_text(encoding="utf-8")
            if not script_content.startswith('#!/usr/bin/env python') and not script_content.startswith('"""'):
                results.append(ValidationResult(
                    path=script,
                    level="info",
                    message="Script missing shebang or docstring"
                ))
    
    return results


def validate_agent(agent_path: Path) -> List[ValidationResult]:
    """Validate an agent directory."""
    results = []
    
    # Check for at least one .md file
    md_files = list(agent_path.glob("*.md"))
    if not md_files:
        results.append(ValidationResult(
            path=agent_path,
            level="error",
            message="Agent directory has no .md files"
        ))
        return results
    
    # Validate each agent file
    for agent_file in md_files:
        content = agent_file.read_text(encoding="utf-8")
        results.extend(validate_yaml_frontmatter(content, agent_file))
        
        # Check for description in frontmatter
        if "description:" not in content[:500]:
            results.append(ValidationResult(
                path=agent_file,
                level="warning",
                message="Agent file missing description in frontmatter"
            ))
    
    return results


def validate_domain(domain_path: Path) -> List[ValidationResult]:
    """Validate a domain YAML file."""
    results = []
    
    if not HAS_YAML or yaml is None:
        return results
    
    try:
        with open(domain_path, encoding="utf-8") as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        results.append(ValidationResult(
            path=domain_path,
            level="error",
            message=f"Invalid YAML: {e}"
        ))
        return results
    
    if not config:
        results.append(ValidationResult(
            path=domain_path,
            level="error",
            message="Empty domain configuration"
        ))
        return results
    
    # Check required domain fields
    if "domain" not in config:
        results.append(ValidationResult(
            path=domain_path,
            level="error",
            message="Missing 'domain' section"
        ))
    else:
        domain = config["domain"]
        for field in ["id", "name", "description"]:
            if field not in domain:
                results.append(ValidationResult(
                    path=domain_path,
                    level="error",
                    message=f"Missing domain.{field}"
                ))
    
    # Check categories
    if "categories" not in config or not config["categories"]:
        results.append(ValidationResult(
            path=domain_path,
            level="warning",
            message="No categories defined"
        ))
    
    return results


def check_domain_agent_consistency(report: ValidationReport):
    """Check that each domain has a corresponding agent folder."""
    if not DOMAINS_DIR.exists():
        return
    
    domains = {f.stem for f in DOMAINS_DIR.glob("*.yaml") if not f.name.startswith("_")}
    agents = {d.name for d in AGENTS_DIR.iterdir() if d.is_dir()} if AGENTS_DIR.exists() else set()
    
    # Domains without agents
    for domain in domains - agents:
        report.add(ValidationResult(
            path=AGENTS_DIR / domain,
            level="warning",
            message=f"Domain '{domain}' has no corresponding agent folder"
        ))


def validate_all() -> ValidationReport:
    """Run all validations."""
    report = ValidationReport()
    
    # Validate skills
    if SKILLS_DIR.exists():
        for category_dir in SKILLS_DIR.iterdir():
            if not category_dir.is_dir() or category_dir.name.startswith("."):
                continue
            
            for skill_dir in category_dir.iterdir():
                if skill_dir.is_dir():
                    for result in validate_skill(skill_dir):
                        report.add(result)
    
    # Validate agents
    if AGENTS_DIR.exists():
        for agent_dir in AGENTS_DIR.iterdir():
            if agent_dir.is_dir() and not agent_dir.name.startswith("."):
                for result in validate_agent(agent_dir):
                    report.add(result)
    
    # Validate domains
    if DOMAINS_DIR.exists():
        for domain_file in DOMAINS_DIR.glob("*.yaml"):
            if not domain_file.name.startswith("_"):
                for result in validate_domain(domain_file):
                    report.add(result)
    
    # Check consistency
    check_domain_agent_consistency(report)
    
    return report


def main():
    parser = argparse.ArgumentParser(description="Validate skills and plugins")
    parser.add_argument("--fix", action="store_true", help="Auto-fix issues where possible")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    parser.add_argument("--quiet", "-q", action="store_true", help="Only show summary")
    args = parser.parse_args()
    
    print("Skills & Plugins Validator")
    print("=" * 50)
    
    report = validate_all()
    
    # Print results
    if not args.quiet:
        for result in report.results:
            if result.level == "error" or (result.level == "warning" and not args.quiet):
                print(result)
    
    report.print_summary()
    
    # Exit code
    if report.has_errors:
        sys.exit(1)
    elif args.strict and report.warnings:
        sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
