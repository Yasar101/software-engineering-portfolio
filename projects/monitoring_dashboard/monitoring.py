"""Thread-safe rolling metrics for a real-time dashboard."""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from statistics import fmean
from threading import Lock


@dataclass(frozen=True)
class MetricSummary:
    count: int
    current: float
    average: float
    minimum: float
    maximum: float


class MetricWindow:
    def __init__(self, capacity: int = 60) -> None:
        if capacity < 1:
            raise ValueError("capacity must be positive")
        self._values: dict[str, deque[float]] = defaultdict(lambda: deque(maxlen=capacity))
        self._lock = Lock()

    def record(self, name: str, value: float) -> None:
        if not name.strip():
            raise ValueError("metric name is required")
        with self._lock:
            self._values[name].append(float(value))

    def summary(self, name: str) -> MetricSummary | None:
        with self._lock:
            values = tuple(self._values.get(name, ()))
        if not values:
            return None
        return MetricSummary(len(values), values[-1], fmean(values), min(values), max(values))

    def health(self, metric: str, maximum: float) -> str:
        summary = self.summary(metric)
        if summary is None:
            return "unknown"
        return "degraded" if summary.current > maximum else "healthy"
