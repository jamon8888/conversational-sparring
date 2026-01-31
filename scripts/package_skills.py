import os
import shutil
import glob
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def package_skills():
    """Package each skill into a standalone zip file."""
    
    # Configuration
    ROOT_DIR = Path(__file__).parent.parent
    SKILLS_DIR = ROOT_DIR / "skills"
    DIST_DIR = ROOT_DIR / "dist" / "skills"
    
    # Ensure dist directory exists
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Packaging skills from {SKILLS_DIR} to {DIST_DIR}...")
    
    # Find all skills (directories containing SKILL.md)
    # We look 2 levels deep: category/skill/SKILL.md
    skills_packaged = 0
    
    for category_dir in SKILLS_DIR.iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith('.'):
            continue
            
        category_name = category_dir.name
        category_dist_dir = DIST_DIR / category_name
        category_dist_dir.mkdir(exist_ok=True)
            
        for skill_dir in category_dir.iterdir():
            if not skill_dir.is_dir() or skill_dir.name.startswith('.'):
                continue
                
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
                
            skill_name = skill_dir.name
            
            # Create zip archive in the category subdirectory
            archive_path = category_dist_dir / skill_name
            
            logger.info(f"  Zipping {category_name}/{skill_name}...")
            shutil.make_archive(
                str(archive_path),
                'zip',
                root_dir=str(category_dir),
                base_dir=skill_name
            )
            skills_packaged += 1
            
    logger.info(f"\nSuccess! packaged {skills_packaged} skills to {DIST_DIR}")

if __name__ == "__main__":
    package_skills()
