"""A small calculator with explicit operators and predictable decimal results."""

from decimal import Decimal, InvalidOperation
from typing import Callable


class CalculationError(ValueError):
    """Raised when an expression cannot be evaluated safely."""


def _divide(left: Decimal, right: Decimal) -> Decimal:
    if right == 0:
        raise CalculationError("cannot divide by zero")
    return left / right


OPERATIONS: dict[str, Callable[[Decimal, Decimal], Decimal]] = {
    "+": lambda left, right: left + right,
    "-": lambda left, right: left - right,
    "*": lambda left, right: left * right,
    "/": _divide,
}


def calculate(expression: str) -> Decimal:
    """Evaluate a three-token expression such as ``12.5 * 4``."""
    parts = expression.split()
    if len(parts) != 3 or parts[1] not in OPERATIONS:
        raise CalculationError("expected: NUMBER (+|-|*|/) NUMBER")
    try:
        left, right = Decimal(parts[0]), Decimal(parts[2])
    except InvalidOperation as exc:
        raise CalculationError("operands must be numbers") from exc
    return OPERATIONS[parts[1]](left, right)


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Safely calculate a simple expression")
    parser.add_argument("expression", help='for example: "12.5 * 4"')
    args = parser.parse_args()
    try:
        print(calculate(args.expression))
    except CalculationError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
