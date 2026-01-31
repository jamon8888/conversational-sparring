"""SQLite-backed event ledger for the Conversational Sparring Partner.

Adapted from PMM's event_log.py with simplified event kinds for sparring.
Provides append-only, hash-chained storage for goals, reflections, patterns, and feedback.
"""

from __future__ import annotations

import json
import os
import sqlite3
import threading
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Any, Dict, List, Optional


# Valid event kinds for the sparring system
EVENT_KINDS = frozenset([
    "goal_open",        # User sets a goal
    "goal_close",       # Goal completed successfully
    "goal_abandon",     # Goal abandoned with reason
    "reflection",       # Structured reflection {intent, outcome, next}
    "struggle",         # Detected struggle/blocker
    "intervention",     # Sparring offered help
    "feedback",         # Sparring feedback given
    "pattern_detected", # Behavioral pattern identified
    "achievement",      # Milestone reached
    "config",           # User preferences
    "session_start",    # New sparring session began
    "session_end",      # Sparring session ended
    "domain_change",    # Domain changed during session
    "rsm_snapshot",     # Periodic self-model checkpoint
    "tendency_detected",# Behavioral tendency identified
    "meta_pattern",     # Pattern of patterns detected
    "cognitive_mode_switch", # Decision vs Learning switch
    "ere_adjustment",   # Element Interactivity Level change
    "sdt_assessment",   # Autonomy/Competence/Relatedness check
    # Skill marketplace events
    "skill_install",    # User installed a skill
    "skill_uninstall",  # User removed a skill
    "skill_use",        # User invoked a skill
    "bundle_install",   # User installed a skill bundle
    "skill_feedback",   # User rated/reviewed a skill
])


def _iso_now() -> str:
    """Return current UTC timestamp in ISO format."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def _canonical_json(obj: Any) -> str:
    """Return canonical JSON string for deterministic hashing."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def get_default_db_path() -> str:
    """Return the default database path (~/.claude/sparring/sparring.db)."""
    sparring_dir = Path.home() / ".claude" / "sparring"
    sparring_dir.mkdir(parents=True, exist_ok=True)
    return str(sparring_dir / "sparring.db")


class SparringLedger:
    """Persistent append-only ledger for sparring events with hash chaining."""

    def __init__(self, path: Optional[str] = None) -> None:
        """Initialize ledger with SQLite database.

        Args:
            path: Database file path. Defaults to ~/.claude/sparring/sparring.db
        """
        self._path = path or get_default_db_path()

        # Ensure parent directory exists
        db_dir = os.path.dirname(self._path)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)

        self._conn = sqlite3.connect(self._path, check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._lock = threading.RLock()
        self._listeners: List = []
        self._init_db()

    def _init_db(self) -> None:
        """Create tables and indexes if they don't exist."""
        with self._conn:
            self._conn.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ts TEXT NOT NULL,
                    kind TEXT NOT NULL,
                    content TEXT NOT NULL,
                    meta TEXT NOT NULL,
                    prev_hash TEXT,
                    hash TEXT
                );
            """)
            # Index for efficient tail queries
            self._conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_events_id_desc ON events(id DESC);"
            )
            # Index for kind-based queries
            self._conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_kind ON events(kind);"
            )
            # Unique hash index for idempotent appends
            self._conn.execute(
                "CREATE UNIQUE INDEX IF NOT EXISTS idx_events_hash ON events(hash);"
            )

    def register_listener(self, callback) -> None:
        """Register a callback to be called when events are appended."""
        with self._lock:
            self._listeners.append(callback)

    def _emit(self, ev: Dict[str, Any]) -> None:
        """Notify all listeners of a new event."""
        for cb in list(self._listeners):
            try:
                cb(ev)
            except Exception:
                pass  # Listeners should not break the ledger

    def _last_hash(self) -> Optional[str]:
        """Get the hash of the most recent event."""
        with self._lock:
            cur = self._conn.execute(
                "SELECT hash FROM events ORDER BY id DESC LIMIT 1"
            )
            row = cur.fetchone()
            return row[0] if row and row[0] else None

    def append(
        self,
        *,
        kind: str,
        content: str,
        meta: Optional[Dict[str, Any]] = None
    ) -> int:
        """Append an event to the ledger.

        Args:
            kind: Event type (must be in EVENT_KINDS)
            content: Event content (typically JSON)
            meta: Optional metadata dict

        Returns:
            Event ID

        Raises:
            ValueError: If kind is invalid
            TypeError: If content is not a string
        """
        if kind not in EVENT_KINDS:
            raise ValueError(f"Invalid event kind: {kind}. Valid: {sorted(EVENT_KINDS)}")
        if not isinstance(content, str):
            raise TypeError("content must be a string")

        meta = meta or {}
        ts = _iso_now()
        prev_hash = self._last_hash()

        # Build hash payload (excludes timestamp for determinism)
        payload = {
            "kind": kind,
            "content": content,
            "meta": meta,
            "prev_hash": prev_hash,
        }
        digest = sha256(_canonical_json(payload).encode("utf-8")).hexdigest()

        with self._lock, self._conn:
            # Idempotent insert using UNIQUE(hash)
            cur = self._conn.execute(
                """INSERT OR IGNORE INTO events
                   (ts, kind, content, meta, prev_hash, hash)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (ts, kind, content, _canonical_json(meta), prev_hash, digest),
            )

            if cur.rowcount == 0:
                # Event with same hash already exists
                cur_row = self._conn.execute(
                    "SELECT * FROM events WHERE hash = ?", (digest,)
                )
                row = cur_row.fetchone()
                if row is None:
                    raise RuntimeError("Hash conflict without row")
                ev_id = int(row["id"])
                ts_db = row["ts"]
            else:
                # lastrowid is always set when rowcount > 0
                assert cur.lastrowid is not None
                ev_id = int(cur.lastrowid)
                ts_db = ts

        ev = {
            "id": ev_id,
            "ts": ts_db,
            "kind": kind,
            "content": content,
            "meta": meta,
            "prev_hash": prev_hash,
            "hash": digest,
        }
        self._emit(ev)
        return ev_id

    def read_all(self) -> List[Dict[str, Any]]:
        """Read all events in chronological order."""
        with self._lock:
            cur = self._conn.execute("SELECT * FROM events ORDER BY id ASC")
            return [self._row_to_dict(row) for row in cur.fetchall()]

    def read_tail(self, limit: int) -> List[Dict[str, Any]]:
        """Read the most recent events."""
        with self._lock:
            cur = self._conn.execute(
                "SELECT * FROM events ORDER BY id DESC LIMIT ?", (limit,)
            )
            rows = cur.fetchall()
            rows.reverse()
            return [self._row_to_dict(row) for row in rows]

    def read_by_kind(
        self,
        kind: str,
        limit: Optional[int] = None,
        reverse: bool = False
    ) -> List[Dict[str, Any]]:
        """Read events filtered by kind."""
        order = "DESC" if reverse else "ASC"
        sql = f"SELECT * FROM events WHERE kind = ? ORDER BY id {order}"
        params: List[Any] = [kind]
        if limit is not None:
            sql += " LIMIT ?"
            params.append(int(limit))

        with self._lock:
            cur = self._conn.execute(sql, tuple(params))
            return [self._row_to_dict(row) for row in cur.fetchall()]

    def read_since(self, event_id: int, limit: int = 1000) -> List[Dict[str, Any]]:
        """Read events after the given event ID."""
        with self._lock:
            cur = self._conn.execute(
                "SELECT * FROM events WHERE id > ? ORDER BY id ASC LIMIT ?",
                (int(event_id), int(limit)),
            )
            return [self._row_to_dict(row) for row in cur.fetchall()]

    def get(self, event_id: int) -> Optional[Dict[str, Any]]:
        """Get a single event by ID."""
        with self._lock:
            cur = self._conn.execute(
                "SELECT * FROM events WHERE id = ?", (event_id,)
            )
            row = cur.fetchone()
            return self._row_to_dict(row) if row else None

    def last_of_kind(self, kind: str) -> Optional[Dict[str, Any]]:
        """Get the most recent event of a given kind."""
        with self._lock:
            cur = self._conn.execute(
                "SELECT * FROM events WHERE kind = ? ORDER BY id DESC LIMIT 1",
                (kind,),
            )
            row = cur.fetchone()
            return self._row_to_dict(row) if row else None

    def count(self) -> int:
        """Return total event count."""
        with self._lock:
            cur = self._conn.execute("SELECT COUNT(*) FROM events")
            row = cur.fetchone()
            return int(row[0]) if row else 0

    def count_by_kind(self, kind: str) -> int:
        """Return count of events of a specific kind."""
        with self._lock:
            cur = self._conn.execute(
                "SELECT COUNT(*) FROM events WHERE kind = ?", (kind,)
            )
            return cur.fetchone()[0]

    def hash_sequence(self) -> List[str]:
        """Return all event hashes in order (for integrity verification)."""
        with self._lock:
            cur = self._conn.execute("SELECT hash FROM events ORDER BY id ASC")
            return [r[0] for r in cur.fetchall()]

    def verify_chain(self) -> bool:
        """Verify the hash chain integrity."""
        events = self.read_all()
        for i, event in enumerate(events):
            expected_prev = events[i - 1]["hash"] if i > 0 else None
            if event["prev_hash"] != expected_prev:
                return False
            # Recompute hash
            payload = {
                "kind": event["kind"],
                "content": event["content"],
                "meta": event["meta"],
                "prev_hash": event["prev_hash"],
            }
            computed = sha256(_canonical_json(payload).encode("utf-8")).hexdigest()
            if computed != event["hash"]:
                return False
        return True

    def _row_to_dict(self, row: sqlite3.Row) -> Dict[str, Any]:
        """Convert a database row to a dict."""
        return {
            "id": row["id"],
            "ts": row["ts"],
            "kind": row["kind"],
            "content": row["content"],
            "meta": json.loads(row["meta"] or "{}"),
            "prev_hash": row["prev_hash"],
            "hash": row["hash"],
        }

    def close(self) -> None:
        """Close the database connection."""
        with self._lock:
            self._conn.close()

    # Domain tracking helpers

    def start_session(self, domain_id: str = "developer") -> int:
        """Start a new sparring session with specified domain.

        Args:
            domain_id: Domain identifier for this session

        Returns:
            Event ID
        """
        content = json.dumps({
            "domain": domain_id,
        }, sort_keys=True)

        return self.append(
            kind="session_start",
            content=content,
            meta={"domain": domain_id},
        )

    def change_domain(self, domain_id: str) -> int:
        """Record a domain change during session.

        Args:
            domain_id: New domain identifier

        Returns:
            Event ID
        """
        content = json.dumps({
            "domain": domain_id,
        }, sort_keys=True)

        return self.append(
            kind="domain_change",
            content=content,
            meta={"domain": domain_id},
        )

    def get_current_domain(self) -> Optional[str]:
        """Get the most recent domain from session or domain_change events.

        Returns:
            Domain ID or None if no domain set
        """
        # Check for most recent domain change
        domain_change = self.last_of_kind("domain_change")
        session_start = self.last_of_kind("session_start")

        latest = None
        latest_id = 0

        if domain_change and domain_change.get("id", 0) > latest_id:
            latest = domain_change
            latest_id = domain_change.get("id", 0)

        if session_start and session_start.get("id", 0) > latest_id:
            latest = session_start

        if latest:
            return latest.get("meta", {}).get("domain")

        return None

