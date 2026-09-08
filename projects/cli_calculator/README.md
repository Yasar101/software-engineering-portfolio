# Python CLI Calculator

**TESTED** · [Portfolio](../../README.md) · [Architecture](../../docs/ARCHITECTURE.md)

A command-line calculator for one explicit binary operation.

## Purpose and engineering skills

Practice input validation and predictable decimal arithmetic without executing input as code.

## Structure

calculator.py separates parsing, an operator table and the CLI. [Source](calculator.py).

## Run

From the repository root with Python 3.11+, run this offline example using `python3` (no dependencies or credentials):

```python
from projects.cli_calculator import calculate
assert str(calculate("12.5 * 4")) == "50.0"
print(calculate("0.1 + 0.2"))
```

## Test

```sh
python3 -m unittest tests.test_foundations.CalculatorTests -v
python3 -m unittest discover -s tests -v
```

The full suite also includes release regression tests and executes these README examples.

## Complete and remaining

**Complete:** Four operators, malformed-input rejection, divide-by-zero handling and finite-number validation.

**Remaining / limitations:** No expression grammar, history or UI. Decimal arithmetic uses the current finite-precision context; extreme magnitudes can raise decimal errors.

## Learning takeaway

An explicit grammar makes accepted inputs and error behavior easier to explain than dynamic evaluation.
