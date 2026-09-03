"""REST-ready item service with a replaceable persistence port."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Protocol


@dataclass(frozen=True)
class Item:
    id: int
    name: str
    price_pence: int


class ItemRepository(Protocol):
    def add(self, name: str, price_pence: int) -> Item: ...
    def get(self, item_id: int) -> Item | None: ...
    def all(self) -> list[Item]: ...


class MemoryItemRepository:
    """Test adapter matching the interface expected of a PostgreSQL adapter."""

    def __init__(self) -> None:
        self._items: dict[int, Item] = {}

    def add(self, name: str, price_pence: int) -> Item:
        item = Item(len(self._items) + 1, name, price_pence)
        self._items[item.id] = item
        return item

    def get(self, item_id: int) -> Item | None:
        return self._items.get(item_id)

    def all(self) -> list[Item]:
        return list(self._items.values())


class ItemService:
    def __init__(self, repository: ItemRepository) -> None:
        self.repository = repository

    def create(self, payload: dict[str, object]) -> tuple[int, dict[str, object]]:
        name = str(payload.get("name", "")).strip()
        price = payload.get("price_pence")
        if not name or not isinstance(price, int) or isinstance(price, bool) or price < 0:
            return 422, {"error": "name and non-negative integer price_pence are required"}
        return 201, asdict(self.repository.add(name, price))

    def retrieve(self, item_id: int) -> tuple[int, dict[str, object]]:
        item = self.repository.get(item_id)
        return (200, asdict(item)) if item else (404, {"error": "item not found"})

    def list(self) -> tuple[int, dict[str, object]]:
        return 200, {"items": [asdict(item) for item in self.repository.all()]}


POSTGRES_SCHEMA = """
CREATE TABLE IF NOT EXISTS items (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL CHECK (length(trim(name)) > 0),
    price_pence INTEGER NOT NULL CHECK (price_pence >= 0)
);
"""
