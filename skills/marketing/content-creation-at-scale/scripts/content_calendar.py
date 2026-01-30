#!/usr/bin/env python3
"""
Content Calendar Manager

Create, schedule, and track content across platforms.

Usage:
    python content_calendar.py --create --days 30
    python content_calendar.py --add post.md --date 2025-01-15 --platform twitter
    python content_calendar.py --view --month 2025-01
"""

import argparse
import csv
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict

class ContentCalendar:
    """Manage content calendar"""
    
    def __init__(self, calendar_file: Path = Path("content-calendar.json")):
        self.calendar_file = calendar_file
        self.calendar = self.load()
    
    def load(self) -> Dict:
        """Load calendar from file"""
        if self.calendar_file.exists():
            with open(self.calendar_file, 'r') as f:
                return json.load(f)
        return {"entries": []}
    
    def save(self):
        """Save calendar to file"""
        with open(self.calendar_file, 'w') as f:
            json.dump(self.calendar, f, indent=2)
    
    def add_entry(self, date: str, platform: str, content_file: str, topic: str = ""):
        """Add content to calendar"""
        entry = {
            "date": date,
            "platform": platform,
            "content_file": content_file,
            "topic": topic,
            "status": "scheduled"
        }
        self.calendar["entries"].append(entry)
        self.save()
        print(f"✅ Added to calendar: {date} - {platform}")
    
    def view(self, month: str = None):
        """View calendar entries"""
        entries = self.calendar["entries"]
        
        if month:
            entries = [e for e in entries if e["date"].startswith(month)]
        
        print(f"\n📅 Content Calendar ({len(entries)} entries)\n")
        for entry in sorted(entries, key=lambda x: x["date"]):
            print(f"{entry['date']} | {entry['platform']:10} | {entry['topic']}")
    
    def export_csv(self, output_file: Path):
        """Export calendar to CSV"""
        with open(output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["date", "platform", "topic", "status"])
            writer.writeheader()
            writer.writerows(self.calendar["entries"])
        print(f"✅ Exported to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Content Calendar Manager")
    parser.add_argument("--create", action="store_true", help="Create new calendar")
    parser.add_argument("--add", type=Path, help="Add content file to calendar")
    parser.add_argument("--date", help="Schedule date (YYYY-MM-DD)")
    parser.add_argument("--platform", help="Platform name")
    parser.add_argument("--topic", default="", help="Content topic")
    parser.add_argument("--view", action="store_true", help="View calendar")
    parser.add_argument("--month", help="Filter by month (YYYY-MM)")
    parser.add_argument("--export", type=Path, help="Export to CSV")
    
    args = parser.parse_args()
    
    calendar = ContentCalendar()
    
    if args.create:
        print("✅ Calendar initialized")
    elif args.add:
        if not args.date or not args.platform:
            print("Error: --add requires --date and --platform")
            sys.exit(1)
        calendar.add_entry(args.date, args.platform, str(args.add), args.topic)
    elif args.view:
        calendar.view(args.month)
    elif args.export:
        calendar.export_csv(args.export)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
