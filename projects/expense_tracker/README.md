# Personal Expense Tracker

**TESTED** · [Portfolio](../../README.md) · [Architecture](../../docs/ARCHITECTURE.md) · [Live demo](https://yasar101.github.io/software-engineering-portfolio/demos/expense-tracker.html)

A local expense model with category/monthly totals and JSON save/load.

## Purpose and engineering skills

Explore domain modelling, money representation and persistence round trips.

## Structure

tracker.py contains an immutable Expense and a tracker with a JSON adapter. [Source](tracker.py).

## Run

From the repository root with Python 3.11+, run this offline example using `python3` (no dependencies or credentials):

```python
from datetime import date
from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory
from projects.expense_tracker import Expense, ExpenseTracker
tracker = ExpenseTracker([Expense(Decimal("4.50"), "food", date(2026, 9, 1))])
with TemporaryDirectory() as directory:
    path = Path(directory) / "expenses.json"
    tracker.save(path)
    assert ExpenseTracker.load(path).total_for_month(2026, 9) == Decimal("4.50")
```

## Test

```sh
python3 -m unittest tests.test_foundations.ExpenseTests -v
python3 -m unittest discover -s tests -v
```

The full suite also includes release regression tests and executes these README examples.

## Complete and remaining

**Complete:** Positive-amount/category validation, reports and a tested save/load round trip.

**Remaining / limitations:** No UI, encryption, atomic writes, concurrent-writer support or comprehensive corrupt-file recovery. Use synthetic data for evaluation.

## Learning takeaway

Serializing decimals as strings preserves money values across JSON round trips.

## Command-line demonstration
Run a real local persistence flow:

```bash
python3 -m projects.expense_tracker --file expenses.json add 12.50 food --note "Lunch"
python3 -m projects.expense_tracker --file expenses.json list
python3 -m projects.expense_tracker --file expenses.json list --category food --month 2026-09
python3 -m projects.expense_tracker --file expenses.json summary --month 2026-09
```

`expenses.json` is local user data and should not be committed.
