# REST Service / PostgreSQL Reference

**REFERENCE IMPLEMENTATION** · [Portfolio](../../README.md) · [Architecture](../../docs/ARCHITECTURE.md)

A transport-neutral item service returning status codes and dictionaries, with a repository protocol and illustrative SQL schema.

## Purpose and engineering skills

Practice validation and separate service behavior from persistence and HTTP frameworks.

## Structure

api.py contains ItemService, ItemRepository, MemoryItemRepository and POSTGRES_SCHEMA. [Source](api.py).

## Run

From the repository root with Python 3.11+, run this offline example using `python3` (no dependencies or credentials):

```python
from projects.postgres_rest_api import ItemService, MemoryItemRepository
service = ItemService(MemoryItemRepository())
status, item = service.create({"name": "Keyboard", "price_pence": 7500})
assert status == 201
assert service.retrieve(item["id"]) == (200, item)
print(service.list())
```

## Test

```sh
python3 -m unittest tests.test_systems.ApiTests -v
python3 -m unittest discover -s tests -v
```

The full suite also includes release regression tests and executes these README examples.

## Complete and remaining

**Complete:** Create/list/retrieve service behavior; 201/200/404/422 semantics; non-negative integer pricing and string-name validation.

**Remaining / limitations:** No HTTP server, PostgreSQL driver/connection, migrations or authentication. The schema has not been executed against PostgreSQL. This is not a running REST deployment.

## Learning takeaway

A protocol makes the intended persistence boundary reviewable without pretending a live adapter exists.

## Command-line demonstration
Run a local HTTP demonstration (uses the in-memory adapter, not PostgreSQL):

```bash
python3 -m projects.postgres_rest_api
curl http://127.0.0.1:8001/health
curl -X POST http://127.0.0.1:8001/items -H 'Content-Type: application/json' -d '{"name":"Keyboard","price_pence":7500}'
```
