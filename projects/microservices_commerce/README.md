# Commerce Workflow Core

**TESTED CORE** · [Portfolio](../../README.md) · [Architecture](../../docs/ARCHITECTURE.md)

An in-process order workflow with pricing, stock reservation and an injected payment callback.

## Purpose and engineering skills

Explore service boundaries and compensation when a downstream operation fails.

## Structure

commerce.py separates Inventory, immutable Order and CommerceService. [Source](commerce.py).

## Run

From the repository root with Python 3.11+, run this offline example using `python3` (no dependencies or credentials):

```python
from decimal import Decimal
from projects.microservices_commerce import CommerceService, Inventory
inventory = Inventory({"book": 2})
service = CommerceService(inventory, {"book": Decimal("12.50")})
print(service.place_order("book", 1, lambda total: True))
service.place_order("book", 1, lambda total: False)
assert inventory.stock["book"] == 1
```

## Test

```sh
python3 -m unittest tests.test_systems.CommerceTests -v
python3 -m unittest discover -s tests -v
```

The full suite also includes release regression tests and executes these README examples.

## Complete and remaining

**Complete:** Success, payment rejection, unavailable stock and local reservation compensation. Payment exceptions restore local stock and propagate.

**Remaining / limitations:** No deployed microservices, database transaction, locking, idempotency or durable saga. A payment timeout may have charged the customer: reconciliation is required before retrying.

## Learning takeaway

Compensation restores local state; it cannot prove or reverse an external payment outcome.
