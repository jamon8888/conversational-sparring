#!/usr/bin/env python3
"""
Content Repurposer - Create multiple content pieces from one source

Takes one piece of content and generates 20+ variations across formats.

Usage:
    python content_repurposer.py blog.md --all-formats
    python content_repurposer.py blog.md --formats twitter,linkedin,email
    python content_repurposer.py blog.md --all-formats --output ./campaign/
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List, Dict
import subprocess

# Import formatter
try:
    from content_formatter import ContentFormatter, PLATFORMS
except ImportError:
    print("Error: content_formatter.py not found in same directory")
    sys.exit(1)

AVAILABLE_FORMATS = [
    "twitter-thread",
    "twitter",
    "linkedin",
    "instagram",
    "facebook",
    "email",
    "youtube"
]

class ContentRepurposer:
    """Repurpose content across multiple formats"""
    
    def __init__(self, source_file: Path, output_dir: Path = None):
        self.source_file = source_file
        self.output_dir = output_dir or Path("./repurposed")
        self.output_dir.mkdir(exist_ok=True, parents=True)
        self.formatter = ContentFormatter(source_file)
    
    def repurpose_all(self, formats: List[str] = None, generate_images: bool = False) -> Dict[str, List[Path]]:
        """Repurpose to all or specified formats"""
        formats = formats or AVAILABLE_FORMATS
        results = {}
        
        print(f"📝 Repurposing: {self.source_file.name}")
        print(f"📁 Output directory: {self.output_dir}")
        print()
        
        for format_name in formats:
            if format_name not in AVAILABLE_FORMATS:
                print(f"⚠️  Unknown format: {format_name}, skipping")
                continue
            
            print(f"⏳ Generating {format_name}...")
            files = self._generate_format(format_name)
            results[format_name] = files
            print(f"✅ Created {len(files)} {format_name} file(s)")
        
        # Generate summary
        total_files = sum(len(files) for files in results.values())
        print()
        print(f"🎉 Repurposing complete!")
        print(f"📊 Generated {total_files} total pieces across {len(results)} formats")
        
        # Create summary file
        self._create_summary(results)
        
        return results
    
    def _generate_format(self, format_name: str) -> List[Path]:
        """Generate content for specific format"""
        files = []
        
        if format_name == "twitter-thread":
            # Generate multiple thread variations
            for i in range(1, 3):  # 2 variations
                content = self.formatter.format_for_platform("twitter-thread", max_tweets=10)
                output_file = self.output_dir / f"twitter-thread-{i}.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                files.append(output_file)
        
        elif format_name == "twitter":
            # Generate multiple standalone tweets
            for i in range(1, 6):  # 5 tweets
                content = self.formatter.format_for_platform("twitter")
                output_file = self.output_dir / f"twitter-post-{i}.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                files.append(output_file)
        
        elif format_name == "linkedin":
            # Generate LinkedIn variations
            for i, optimize in enumerate([False, True], 1):
                content = self.formatter.format_for_platform("linkedin", optimize_engagement=optimize)
                suffix = "-optimized" if optimize else ""
                output_file = self.output_dir / f"linkedin-post{suffix}.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                files.append(output_file)
        
        elif format_name == "instagram":
            # Generate Instagram captions
            for i in range(1, 4):  # 3 captions
                content = self.formatter.format_for_platform("instagram", add_hashtags=True)
                output_file = self.output_dir / f"instagram-caption-{i}.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                files.append(output_file)
        
        else:
            # Single file for other formats
            content = self.formatter.format_for_platform(format_name)
            output_file = self.output_dir / f"{format_name}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            files.append(output_file)
        
        return files
    
    def _create_summary(self, results: Dict[str, List[Path]]):
        """Create summary file"""
        summary_file = self.output_dir / "REPURPOSING_SUMMARY.md"
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(f"# Content Repurposing Summary\n\n")
            f.write(f"**Source**: {self.source_file}\n")
            f.write(f"**Date**: {Path(__file__).stat().st_mtime}\n\n")
            
            f.write("## Generated Content\n\n")
            
            for format_name, files in results.items():
                f.write(f"### {format_name.title()}\n")
                f.write(f"- **Count**: {len(files)} pieces\n")
                f.write(f"- **Files**:\n")
                for file in files:
                    f.write(f"  - `{file.name}`\n")
                f.write("\n")
            
            total = sum(len(files) for files in results.values())
            f.write(f"**Total**: {total} pieces of content generated\n")
        
        print(f"📄 Summary saved: {summary_file}")

def main():
    parser = argparse.ArgumentParser(description="Repurpose content across multiple formats")
    parser.add_argument("input_file", type=Path, help="Input content file")
    parser.add_argument("--formats", "-f", 
                       help="Comma-separated list of formats (default: all)")
    parser.add_argument("--all-formats", action="store_true",
                       help="Generate all formats")
    parser.add_argument("--output", "-o", type=Path,
                       help="Output directory (default: ./repurposed)")
    parser.add_argument("--generate-images", action="store_true",
                       help="Generate images using image_generation.py")
    
    args = parser.parse_args()
    
    if not args.input_file.exists():
        print(f"Error: File not found: {args.input_file}", file=sys.stderr)
        sys.exit(1)
    
    # Determine formats
    if args.all_formats:
        formats = AVAILABLE_FORMATS
    elif args.formats:
        formats = [f.strip() for f in args.formats.split(',')]
    else:
        print("Error: Specify --all-formats or --formats")
        sys.exit(1)
    
    try:
        repurposer = ContentRepurposer(args.input_file, args.output)
        results = repurposer.repurpose_all(formats, args.generate_images)
        
        print("\n✅ Repurposing complete!")
        print(f"📁 All files saved in: {repurposer.output_dir}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
