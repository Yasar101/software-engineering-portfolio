"""Runnable, dependency-free demonstrations of the portfolio's real domain code.

This is intentionally a local demo harness, not a production web server.  It keeps
external calls opt-in and marks all seeded values as demonstration data.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from dataclasses import asdict
from datetime import date, datetime
from decimal import Decimal
from enum import Enum

from projects.ai_developer_assistant.assistant import ContextDocument, DeveloperAssistant
from projects.cli_calculator.calculator import calculate
from projects.distributed_ai_platform.scheduler import JobScheduler
from projects.energy_calculator.energy import estimate_energy
from projects.expense_tracker.tracker import Expense, ExpenseTracker
from projects.microservices_commerce.commerce import CommerceService, Inventory
from projects.monitoring_dashboard.monitoring import MetricWindow
from projects.postgres_rest_api.api import ItemService, MemoryItemRepository
from projects.task_manager.tasks import TaskRepository
from projects.weather_dashboard.weather import parse_open_meteo


def _json(value: object) -> None:
    def convert(item: object) -> object:
        if isinstance(item, Decimal):
            return str(item)
        if isinstance(item, (date, datetime)):
            return item.isoformat()
        if isinstance(item, Enum):
            return item.value
        if hasattr(item, "__dataclass_fields__"):
            return {key: convert(val) for key, val in asdict(item).items()}
        if isinstance(item, dict):
            return {str(key): convert(val) for key, val in item.items()}
        if isinstance(item, (list, tuple)):
            return [convert(entry) for entry in item]
        return item

    print(json.dumps(convert(value), indent=2, sort_keys=True))


def calculator(args: argparse.Namespace) -> None:
    _json({"expression": args.expression, "result": calculate(args.expression)})


def expenses(_: argparse.Namespace) -> None:
    tracker = ExpenseTracker([
        Expense(Decimal("32.40"), "food", date(2026, 9, 1), "Demo groceries"),
        Expense(Decimal("14.20"), "travel", date(2026, 9, 2), "Demo journey"),
    ])
    _json({"data": "seeded demo data", "expenses": tracker.expenses,
           "september_total": tracker.total_for_month(2026, 9),
           "by_category": tracker.totals_by_category()})


def weather(_: argparse.Namespace) -> None:
    snapshot = parse_open_meteo({"current": {"temperature_2m": 17.8, "wind_speed_10m": 11.3,
                                                "time": "2026-09-04T12:00"}})
    _json({"data": "local provider-shaped fixture; no network call", "summary": snapshot.summary,
           "observed_at": snapshot.observed_at})


def tasks(_: argparse.Namespace) -> None:
    repository = TaskRepository(sqlite3.connect(":memory:"))
    first = repository.create("Review accessibility states")
    repository.create("Prepare local demonstration")
    repository.complete(first.id)
    _json({"storage": "temporary SQLite database", "all_tasks": repository.list(),
           "completed": repository.list(True), "open": repository.list(False)})


def energy(args: argparse.Namespace) -> None:
    estimate = estimate_energy(Decimal(args.watts), Decimal(args.hours), args.days, Decimal(args.tariff))
    _json({"data": "user-supplied calculation", "watts": args.watts, "hours_per_day": args.hours,
           "days": args.days, "tariff_per_kwh": args.tariff, "estimate": estimate})


def api(_: argparse.Namespace) -> None:
    service = ItemService(MemoryItemRepository())
    created_status, created = service.create({"name": "Demo keyboard", "price_pence": 7500})
    invalid_status, invalid = service.create({"name": "", "price_pence": -1})
    _json({"adapter": "in-memory reference repository; PostgreSQL is not connected",
           "create": {"status": created_status, "body": created},
           "validation": {"status": invalid_status, "body": invalid}, "list": service.list()[1]})


def monitoring(_: argparse.Namespace) -> None:
    metrics = MetricWindow(capacity=4)
    for value in (112, 128, 146, 121):
        metrics.record("latency_ms", value)
    _json({"data": "seeded simulated telemetry", "window": metrics.summary("latency_ms"),
           "health_at_130ms": metrics.health("latency_ms", 130)})


def commerce(args: argparse.Namespace) -> None:
    inventory = Inventory({"demo-book": 2})
    service = CommerceService(inventory, {"demo-book": Decimal("12.50")})
    order = service.place_order("demo-book", 1, lambda _: not args.fail_payment)
    _json({"data": "fictional demo transaction", "payment_result": "declined" if args.fail_payment else "accepted",
           "order": order, "stock_after": inventory.stock,
           "note": "A declined payment releases the reservation."})


def assistant(_: argparse.Namespace) -> None:
    documents = [ContextDocument("auth.py", "OAuth token refresh handler lives here."),
                 ContextDocument("money.py", "Decimal calculations avoid floating point rounding.")]
    assistant = DeveloperAssistant(documents, lambda prompt: "Local demo provider received bounded repository context.")
    question = "Where is token refresh handled?"
    _json({"provider": "local deterministic demo provider; no API key", "question": question,
           "retrieved": [document.path for document in assistant.retrieve(question)], "answer": assistant.answer(question)})


def scheduler(args: argparse.Namespace) -> None:
    scheduler = JobScheduler(max_attempts=2)
    submitted = scheduler.submit({"model": "demo-small", "data": "fictional"})
    claimed = scheduler.claim("demo-worker", lease_seconds=30)
    assert claimed is not None
    finished = scheduler.finish(claimed.id, "demo-worker", not args.fail)
    _json({"infrastructure": "in-process scheduler; workers are simulated", "submitted": submitted,
           "finished": finished})


def main() -> None:
    parser = argparse.ArgumentParser(description="Run honest local demonstrations of portfolio projects.")
    commands = parser.add_subparsers(dest="project", required=True)
    command = commands.add_parser("calculator"); command.add_argument("expression"); command.set_defaults(func=calculator)
    commands.add_parser("expenses").set_defaults(func=expenses)
    commands.add_parser("weather").set_defaults(func=weather)
    commands.add_parser("tasks").set_defaults(func=tasks)
    command = commands.add_parser("energy"); command.add_argument("--watts", default="850"); command.add_argument("--hours", default="3.5"); command.add_argument("--days", type=int, default=30); command.add_argument("--tariff", default="0.28"); command.set_defaults(func=energy)
    commands.add_parser("api").set_defaults(func=api)
    commands.add_parser("monitoring").set_defaults(func=monitoring)
    command = commands.add_parser("commerce"); command.add_argument("--fail-payment", action="store_true"); command.set_defaults(func=commerce)
    commands.add_parser("assistant").set_defaults(func=assistant)
    command = commands.add_parser("scheduler"); command.add_argument("--fail", action="store_true"); command.set_defaults(func=scheduler)
    args = parser.parse_args()
    try:
        args.func(args)
    except (ValueError, ArithmeticError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
