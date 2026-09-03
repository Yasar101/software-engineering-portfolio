from datetime import date
from decimal import Decimal
from pathlib import Path
import sqlite3
import tempfile
import unittest

from projects.cli_calculator.calculator import CalculationError, calculate
from projects.energy_calculator.energy import estimate_energy
from projects.expense_tracker.tracker import Expense, ExpenseTracker
from projects.task_manager.tasks import TaskRepository
from projects.weather_dashboard.weather import parse_open_meteo


class CalculatorTests(unittest.TestCase):
    def test_decimal_calculation(self):
        self.assertEqual(calculate("12.5 * 4"), Decimal("50.0"))

    def test_rejects_unsafe_or_invalid_expression(self):
        with self.assertRaises(CalculationError):
            calculate("__import__('os').system('whoami')")
        with self.assertRaises(CalculationError):
            calculate("1 / 0")


class ExpenseTests(unittest.TestCase):
    def test_reports_and_round_trip(self):
        tracker = ExpenseTracker([
            Expense(Decimal("10.50"), "food", date(2026, 9, 1)),
            Expense(Decimal("4.25"), "travel", date(2026, 9, 2)),
            Expense(Decimal("2.00"), "food", date(2026, 8, 1)),
        ])
        self.assertEqual(tracker.totals_by_category()["food"], Decimal("12.50"))
        self.assertEqual(tracker.total_for_month(2026, 9), Decimal("14.75"))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "expenses.json"
            tracker.save(path)
            self.assertEqual(ExpenseTracker.load(path).expenses, tracker.expenses)

    def test_rejects_non_positive_amount(self):
        with self.assertRaises(ValueError):
            Expense(Decimal("0"), "food", date.today())


class WeatherTests(unittest.TestCase):
    def test_parses_provider_response(self):
        result = parse_open_meteo({"current": {"temperature_2m": 18.25, "wind_speed_10m": 9, "time": "2026-09-03T12:00"}})
        self.assertEqual(result.summary, "18.2°C, wind 9.0 km/h")

    def test_rejects_missing_fields(self):
        with self.assertRaises(ValueError):
            parse_open_meteo({"current": {}})


class TaskTests(unittest.TestCase):
    def test_create_complete_and_filter(self):
        repository = TaskRepository(sqlite3.connect(":memory:"))
        task = repository.create("Ship portfolio")
        self.assertFalse(task.completed)
        self.assertTrue(repository.complete(task.id))
        self.assertEqual([item.title for item in repository.list(True)], ["Ship portfolio"])
        self.assertEqual(repository.list(False), [])


class EnergyTests(unittest.TestCase):
    def test_estimate(self):
        result = estimate_energy(Decimal("1000"), Decimal("2"), 30, Decimal("0.30"))
        self.assertEqual(result.kwh, Decimal("60.000"))
        self.assertEqual(result.cost, Decimal("18.00"))
        self.assertEqual(result.carbon_kg, Decimal("12.420"))

    def test_rejects_impossible_hours(self):
        with self.assertRaises(ValueError):
            estimate_energy(Decimal("1"), Decimal("25"), 1, Decimal("1"))


if __name__ == "__main__":
    unittest.main()
