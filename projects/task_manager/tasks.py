"""SQLite-backed task management."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
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

    def delete(self, task_id: int) -> bool:
        cursor = self.connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.connection.commit()
        return cursor.rowcount == 1

    def list(self, completed: bool | None = None) -> list[Task]:
        sql, params = "SELECT id, title, completed, created_at FROM tasks", ()
        if completed is not None:
            sql, params = sql + " WHERE completed = ?", (int(completed),)
        rows = self.connection.execute(sql + " ORDER BY id", params).fetchall()
        return [Task(row[0], row[1], bool(row[2]), row[3]) for row in rows]


def main() -> None:
    """Manage a persistent local task database without third-party dependencies."""
    import argparse

    parser = argparse.ArgumentParser(description="Manage tasks in a local SQLite database.")
    parser.add_argument("--database", type=Path, default=Path("tasks.sqlite3"), help="SQLite database file")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="create a task")
    add.add_argument("title")
    complete = commands.add_parser("complete", help="mark a task complete")
    complete.add_argument("id", type=int)
    delete = commands.add_parser("delete", help="permanently delete a task")
    delete.add_argument("id", type=int)
    listing = commands.add_parser("list", help="list tasks")
    listing.add_argument("--status", choices=("all", "open", "completed"), default="all")
    args = parser.parse_args()
    repository = TaskRepository(sqlite3.connect(args.database))

    try:
        if args.command == "add":
            task = repository.create(args.title)
            print(f"Created task #{task.id}: {task.title}")
        elif args.command == "complete":
            if not repository.complete(args.id):
                parser.error(f"task #{args.id} was not found")
            print(f"Completed task #{args.id}")
        elif args.command == "delete":
            if not repository.delete(args.id):
                parser.error(f"task #{args.id} was not found")
            print(f"Deleted task #{args.id}")
        else:
            state = {"all": None, "open": False, "completed": True}[args.status]
            tasks = repository.list(state)
            if not tasks:
                print("No matching tasks.")
            for task in tasks:
                print(f"[{'x' if task.completed else ' '}] {task.id}: {task.title}")
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
