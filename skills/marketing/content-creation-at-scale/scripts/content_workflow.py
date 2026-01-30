#!/usr/bin/env python3
"""
Content Workflow Orchestrator

Manage content creation workflows with status tracking.

Usage:
    python content_workflow.py --init blog-workflow
    python content_workflow.py --update post-123 --status review
    python content_workflow.py --view --status all
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List

WORKFLOW_STAGES = ["ideation", "research", "draft", "review", "edit", "approve", "schedule", "publish"]

class WorkflowManager:
    """Manage content workflows"""
    
    def __init__(self, workflow_file: Path = Path("workflow.json")):
        self.workflow_file = workflow_file
        self.workflow = self.load()
    
    def load(self) -> Dict:
        """Load workflow from file"""
        if self.workflow_file.exists():
            with open(self.workflow_file, 'w') as f:
                return json.load(f)
        return {"items": []}
    
    def save(self):
        """Save workflow to file"""
        with open(self.workflow_file, 'w') as f:
            json.dump(self.workflow, f, indent=2)
    
    def add_item(self, item_id: str, title: str, stage: str = "ideation"):
        """Add item to workflow"""
        item = {
            "id": item_id,
            "title": title,
            "stage": stage,
            "created": datetime.now().isoformat(),
            "updated": datetime.now().isoformat()
        }
        self.workflow["items"].append(item)
        self.save()
        print(f"✅ Added: {item_id} - {title}")
    
    def update_status(self, item_id: str, new_stage: str):
        """Update item status"""
        for item in self.workflow["items"]:
            if item["id"] == item_id:
                item["stage"] = new_stage
                item["updated"] = datetime.now().isoformat()
                self.save()
                print(f"✅ Updated {item_id} → {new_stage}")
                return
        print(f"❌ Item not found: {item_id}")
    
    def view_pipeline(self, status_filter: str = "all"):
        """View workflow pipeline"""
        items = self.workflow["items"]
        
        if status_filter != "all":
            items = [i for i in items if i["stage"] == status_filter]
        
        print(f"\n📋 Workflow Pipeline ({len(items)} items)\n")
        
        for stage in WORKFLOW_STAGES:
            stage_items = [i for i in items if i["stage"] == stage]
            if stage_items:
                print(f"\n{stage.upper()} ({len(stage_items)})")
                for item in stage_items:
                    print(f"  • {item['id']}: {item['title']}")

def main():
    parser = argparse.ArgumentParser(description="Content Workflow Manager")
    parser.add_argument("--init", help="Initialize workflow")
    parser.add_argument("--add", help="Add item ID")
    parser.add_argument("--title", help="Item title")
    parser.add_argument("--update", help="Update item ID")
    parser.add_argument("--status", help="New status")
    parser.add_argument("--view", action="store_true", help="View pipeline")
    
    args = parser.parse_args()
    
    wf = WorkflowManager()
    
    if args.init:
        print(f"✅ Workflow initialized: {args.init}")
    elif args.add:
        if not args.title:
            print("Error: --add requires --title")
            sys.exit(1)
        wf.add_item(args.add, args.title)
    elif args.update:
        if not args.status:
            print("Error: --update requires --status")
            sys.exit(1)
        wf.update_status(args.update, args.status)
    elif args.view:
        wf.view_pipeline(args.status or "all")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
