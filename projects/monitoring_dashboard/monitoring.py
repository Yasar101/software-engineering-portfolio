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


def main() -> None:
    """Summarise explicitly supplied local telemetry samples."""
    import argparse

    parser = argparse.ArgumentParser(description="Inspect a bounded local metric window.")
    parser.add_argument("metric", help="metric name, for example latency_ms")
    parser.add_argument("values", nargs="+", type=float, help="one or more numeric samples")
    parser.add_argument("--threshold", type=float, required=True, help="maximum healthy current value")
    parser.add_argument("--capacity", type=int, default=60, help="rolling-window capacity")
    args = parser.parse_args()
    try:
        window = MetricWindow(args.capacity)
        for value in args.values:
            window.record(args.metric, value)
    except ValueError as exc:
        parser.error(str(exc))
    summary = window.summary(args.metric)
    assert summary is not None
    print(f"Metric: {args.metric} (simulated local samples)")
    print(f"Current: {summary.current:g}; average: {summary.average:g}; range: {summary.minimum:g}–{summary.maximum:g}; samples: {summary.count}")
    print(f"Health at threshold {args.threshold:g}: {window.health(args.metric, args.threshold)}")


if __name__ == "__main__":
    main()
