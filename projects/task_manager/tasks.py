"""SQLite-backed task management."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import sqlite3


@dataclass(frozen=True)
class Task:
    id: int
    title: str
    completed: bool
    created_at: str


class TaskRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection
        self.connection.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT NOT NULL, completed INTEGER NOT NULL DEFAULT 0, created_at TEXT NOT NULL)")

    def create(self, title: str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("title is required")
        created_at = datetime.now(timezone.utc).isoformat()
        cursor = self.connection.execute("INSERT INTO tasks(title, created_at) VALUES (?, ?)", (title, created_at))
        self.connection.commit()
        return Task(int(cursor.lastrowid), title, False, created_at)

    def complete(self, task_id: int) -> bool:
        cursor = self.connection.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        self.connection.commit()
        return cursor.rowcount == 1

    def list(self, completed: bool | None = None) -> list[Task]:
        sql, params = "SELECT id, title, completed, created_at FROM tasks", ()
        if completed is not None:
            sql, params = sql + " WHERE completed = ?", (int(completed),)
        rows = self.connection.execute(sql + " ORDER BY id", params).fetchall()
        return [Task(row[0], row[1], bool(row[2]), row[3]) for row in rows]
