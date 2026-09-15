# Energy Calculator

**TESTED** · [Portfolio](../../README.md) · [Architecture](../../docs/ARCHITECTURE.md)

A pure calculation of electricity use, cost and estimated carbon emissions.

## Purpose and engineering skills

Keep domain units, input checks and rounding policy explicit.

## Structure

energy.py exposes estimate_energy and the immutable EnergyEstimate result. [Source](energy.py).

## Run

From the repository root with Python 3.11+, run this offline example using `python3` (no dependencies or credentials):

```python
from decimal import Decimal
from projects.energy_calculator import estimate_energy
result = estimate_energy(Decimal("1000"), Decimal("2"), 30, Decimal("0.30"))
assert result.cost == Decimal("18.00")
print(result)
```

## Test

```sh
python3 -m unittest tests.test_foundations.EnergyTests -v
python3 -m unittest discover -s tests -v
```

The full suite also includes release regression tests and executes these README examples.

## Complete and remaining

**Complete:** Decimal calculations, non-negative-input checks, daily-hour bounds and explicit output rounding.

**Remaining / limitations:** An estimate, not a billing or emissions authority. No UI; caller supplies appropriate tariff/intensity. The default intensity is illustrative, not live-sourced.

## Learning takeaway

Units and rounding choices belong in the domain contract, not just display code.

## Command-line demonstration
Run a transparent local estimate:

```bash
python3 -m projects.energy_calculator --watts 850 --hours 3.5 --days 30 --tariff 0.28
```

This is an estimate from supplied values, not a supplier integration.
