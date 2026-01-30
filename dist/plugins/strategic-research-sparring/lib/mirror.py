"""Mirror projection layer for the Conversational Sparring.

Provides a fast, in-memory queryable state derived deterministically from the
append-only ledger. This allows O(1) queries for open goals, current stats,
and context without scanning the entire database.
"""

from __future__ import annotations

import json
from typing import Any, Dict, List, Optional, Set

from .ledger import SparringLedger


class SparringMirror:
    """Rebuildable in-memory projection of the sparring state.
    
    All state in this class must be strictly derived from ledger events.
    calling rebuild() must produce the exact same state as incremental sync() calls.
    """

    def __init__(self, ledger: SparringLedger) -> None:
        self.ledger = ledger
        self._lock = ledger._lock  # Share lock with ledger for consistency
        
        # State containers
        self.open_goals: Dict[str, Dict[str, Any]] = {}  # goal_id -> goal_event_data
        self.closed_goals: Dict[str, Dict[str, Any]] = {}  # goal_id -> close_event_data
        self.metadata: Dict[str, Any] = {} # Global metadata (user settings etc)
        
        # Metrics & Tracking
        self.reflection_counts: Dict[str, int] = {}  # domain -> count
        self.goal_counts: Dict[str, int] = {}  # domain -> count
        self.current_domain: str = "developer"  # Default domain
        self.last_event_id: int = 0
        
        # Domain tracking
        self.domain_history: List[Dict[str, Any]] = []

    def rebuild(self) -> None:
        """Clear state and replay all events from the ledger."""
        with self._lock:
            # Reset state
            self.open_goals.clear()
            self.closed_goals.clear()
            self.metadata.clear()
            self.reflection_counts.clear()
            self.goal_counts.clear()
            self.current_domain = "developer"
            self.last_event_id = 0
            self.domain_history.clear()

            # Replay all events
            events = self.ledger.read_all()
            for event in events:
                self._apply_event(event)

    def sync(self) -> None:
        """Fetch and apply new events since the last sync."""
        with self._lock:
            # Get new events
            new_events = self.ledger.read_since(self.last_event_id)
            for event in new_events:
                self._apply_event(event)

    def _apply_event(self, event: Dict[str, Any]) -> None:
        """Apply a single event to the state (internal dispatcher)."""
        kind = event["kind"]
        
        # Update high-water mark
        self.last_event_id = max(self.last_event_id, event["id"])

        # Parse content if string
        content = event["content"]
        if isinstance(content, str):
            try:
                data = json.loads(content)
            except json.JSONDecodeError:
                data = {}
        else:
            data = content

        # Dispatch
        if kind == "goal_open":
            self._handle_goal_open(event, data)
        elif kind == "goal_close":
            self._handle_goal_close(event, data)
        elif kind == "goal_abandon":
            self._handle_goal_abandon(event, data)
        elif kind == "session_start":
            self._handle_session_start(event, data)
        elif kind == "domain_change":
            self._handle_domain_change(event, data)
        elif kind == "reflection":
            self._handle_reflection(event, data)
        elif kind == "config":
            self._handle_config(event, data)

    # --- Handlers ---

    def _handle_goal_open(self, event: Dict[str, Any], data: Dict[str, Any]) -> None:
        # data usually contains { "text": "...", "category": "..." }
        # We assume the event ID or a generated UUID is the goal_id. 
        # For simplicity, if 'id' is in data usage that, else key by event ID.
        # But wait, usually PMM goals have a specific ID in the content.
        # Let's assume standard PMM mostly uses the event ID as reference, 
        # or the content has 'goal_id'.
        
        # If the content defines a goal_id, use it. Otherwise use str(event['id'])
        goal_id = data.get("goal_id", str(event["id"]))
        
        goal_entry = {
            "id": goal_id,
            "created_at": event["ts"],
            "text": data.get("text", ""),
            "category": data.get("category", "generic"),
            "domain": self.current_domain,
            "status": "OPEN",
            "open_event_id": event["id"]
        }
        self.open_goals[goal_id] = goal_entry
        
        # Track counts
        d = self.current_domain
        self.goal_counts[d] = self.goal_counts.get(d, 0) + 1

    def _handle_goal_close(self, event: Dict[str, Any], data: Dict[str, Any]) -> None:
        goal_id = data.get("goal_id")
        if goal_id and goal_id in self.open_goals:
            # Move from open to closed
            goal = self.open_goals.pop(goal_id)
            goal["status"] = "CLOSED"
            goal["closed_at"] = event["ts"]
            goal["close_reason"] = data.get("reason", "")
            goal["close_event_id"] = event["id"]
            self.closed_goals[goal_id] = goal

    def _handle_goal_abandon(self, event: Dict[str, Any], data: Dict[str, Any]) -> None:
        goal_id = data.get("goal_id")
        if goal_id and goal_id in self.open_goals:
            goal = self.open_goals.pop(goal_id)
            goal["status"] = "ABANDONED"
            goal["abandoned_at"] = event["ts"]
            goal["abandon_reason"] = data.get("reason", "")
            goal["abandon_event_id"] = event["id"]
            self.closed_goals[goal_id] = goal

    def _handle_session_start(self, event: Dict[str, Any], data: Dict[str, Any]) -> None:
        domain = data.get("domain") or event.get("meta", {}).get("domain")
        if domain:
            self.current_domain = domain

    def _handle_domain_change(self, event: Dict[str, Any], data: Dict[str, Any]) -> None:
        domain = data.get("domain")
        if domain:
            self.current_domain = domain
            self.domain_history.append({
                "ts": event["ts"],
                "domain": domain,
                "event_id": event["id"]
            })

    def _handle_reflection(self, event: Dict[str, Any], data: Dict[str, Any]) -> None:
        d = self.current_domain
        self.reflection_counts[d] = self.reflection_counts.get(d, 0) + 1

    def _handle_config(self, event: Dict[str, Any], data: Dict[str, Any]) -> None:
        # Merge config updates
        self.metadata.update(data)

    # --- Public Queries ---

    def get_open_goals(self, domain: Optional[str] = None) -> List[Dict[str, Any]]:
        """Return list of open goals, optionally filtered by domain."""
        goals = list(self.open_goals.values())
        if domain:
            return [g for g in goals if g["domain"] == domain]
        return goals

    def get_stats(self) -> Dict[str, Any]:
        """Return high-level stats."""
        return {
            "open_goals_count": len(self.open_goals),
            "closed_goals_count": len(self.closed_goals),
            "current_domain": self.current_domain,
            "total_reflections": sum(self.reflection_counts.values())
        }

