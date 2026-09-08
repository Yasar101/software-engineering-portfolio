# SQLite Task Manager

**TESTED** · [Portfolio](../../README.md) · [Architecture](../../docs/ARCHITECTURE.md)

A SQLite repository for creating, completing and filtering tasks.

## Purpose and engineering skills

Practice relational persistence, parameterized SQL and explicit state transitions.

## Structure

tasks.py owns schema creation and repository methods; callers own the SQLite connection. [Source](tasks.py).

## Run

From the repository root with Python 3.11+, run this offline example using `python3` (no dependencies or credentials):

```python
import sqlite3
from projects.task_manager import TaskRepository
connection = sqlite3.connect(":memory:")
try:
    tasks = TaskRepository(connection)
    task = tasks.create("Review a release")
    assert tasks.complete(task.id)
    print(tasks.list(completed=True))
finally:
    connection.close()
```

## Test

```sh
python3 -m unittest tests.test_foundations.TaskTests -v
python3 -m unittest discover -s tests -v
```

The full suite also includes release regression tests and executes these README examples.

## Complete and remaining

**Complete:** Title validation, committed writes, completion and ordered status filtering. Replace :memory: with a file path for persistence.

**Remaining / limitations:** No web interface, authentication, migration system, deletion or multi-user connection management.

## Learning takeaway

Connection ownership and parameterized queries are useful boundaries even in a small repository.
