
import os
import shutil
from pathlib import Path

# Configuration: Map Source Plugin -> List of (Skill Name, Destination Category)
IMPORT_MAP = {
    # MARKETING
    "abm-orchestration": [
        ("account-tiering", "marketing"), 
        ("signal-intel", "marketing")
    ],
    "seo": [
        ("technical-seo", "marketing"), 
        ("keyword-research", "marketing")
    ],
    "growth-experiments": [
        ("growth-loops", "marketing"), 
        ("testing-framework", "marketing")
    ],
    "brand-strategy": [
        ("brand-archetypes", "marketing"), 
        ("visual-identity", "marketing")
    ],
    "social-media-marketing": [
        ("social-calendar-system", "marketing"), 
        ("community-sentiment-dashboard", "marketing")
    ],
    
    # SALES
    "enterprise-sales": [
        ("stakeholder-mapping", "sales"), 
        ("deal-desk", "sales"), 
        ("territory-planning", "sales")
    ],
    "sales-enablement": [
        ("sales-playbooks", "sales"), 
        ("battlecards", "sales") 
    ],
    "sales-prospecting": [
        ("outreach-cadence", "sales"), 
        ("list-building", "sales")
    ],
    "sales-operations": [
        ("commission-modeling", "sales"), 
        ("territory-design", "sales")
    ],
    
    # PRODUCT
    "voice-of-customer": [
        ("customer-feedback-taxonomy", "product"), 
        ("closed-loop-playbook", "product")
    ],
    "product-marketing": [
        ("positioning", "product"), 
        ("launch-plays", "product")
    ],
    "product-launch-orchestration": [
        ("launch-tiering", "product"), 
        ("war-room-ops", "product")
    ],
    
    # ENGINEERING
    "technical-writing": [
        ("api-style-guide", "engineering"), 
        ("doc-requirements-matrix", "engineering")
    ],
    "analytics-pipeline-orchestration": [
        ("instrumentation", "engineering"), 
        ("quality-gates", "engineering")
    ],
    
    # STRATEGIC RESEARCH
    # Note: market-research and competitive-intelligence skills were already present
    "customer-analytics": [
        ("segmentation-framework", "research-strategic"), 
        ("retention-dashboard", "research-strategic")
    ]
}

def import_skills():
    # Setup paths
    BASE_DIR = Path(__file__).parent.parent
    EXTERNAL_PLUGINS_DIR = Path(r"C:\Users\NMarchitecte\Documents\claude-skills\plugins")
    INTERNAL_SKILLS_DIR = BASE_DIR / "skills"
    
    print(f"Importing skills from {EXTERNAL_PLUGINS_DIR} to {INTERNAL_SKILLS_DIR}...\n")
    
    success_count = 0
    skipped_count = 0
    
    for plugin_name, skills_to_import in IMPORT_MAP.items():
        # Source plugin skills directory
        src_plugin_skills = EXTERNAL_PLUGINS_DIR / plugin_name / "skills"
        
        if not src_plugin_skills.exists():
            print(f"Warning: Source plugin directory not found: {src_plugin_skills}")
            continue
            
        for skill_name, dest_category in skills_to_import:
            src_skill_path = src_plugin_skills / skill_name
            dest_category_dir = INTERNAL_SKILLS_DIR / dest_category
            dest_skill_path = dest_category_dir / skill_name
            
            # Check source exists
            if not src_skill_path.exists():
                print(f"  [MISSING] {plugin_name}/{skill_name} not found in source")
                continue
                
            # Check destination (don't overwrite blindly, but maybe we should?)
            # For now, let's copy/overwrite since user approved "import"
            
            if not dest_category_dir.exists():
                dest_category_dir.mkdir(parents=True, exist_ok=True)
                
            try:
                if dest_skill_path.exists():
                    shutil.rmtree(dest_skill_path)
                    
                shutil.copytree(src_skill_path, dest_skill_path)
                print(f"  [COPIED] {skill_name} -> skills/{dest_category}/")
                success_count += 1
            except Exception as e:
                print(f"  [ERROR] Failed to copy {skill_name}: {e}")
                
    print(f"\nImport Complete.")
    print(f"Successfully imported: {success_count} skills")

if __name__ == "__main__":
    import_skills()
