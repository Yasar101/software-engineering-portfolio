# Monitoring Metrics Core

**TESTED CORE** · [Portfolio](../../README.md) · [Architecture](../../docs/ARCHITECTURE.md) · [Live demo](https://yasar101.github.io/software-engineering-portfolio/demos/monitoring-dashboard.html)

A locked, bounded per-metric rolling window with summary and threshold health values.

## Purpose and engineering skills

Explore bounded history, synchronized updates and explicit missing-data behavior.

## Structure

monitoring.py stores deques behind a Lock and returns immutable summaries. [Source](monitoring.py).

## Run

From the repository root with Python 3.11+, run this offline example using `python3` (no dependencies or credentials):

```python
from projects.monitoring_dashboard import MetricWindow
metrics = MetricWindow(capacity=3)
for latency in (1, 2, 3, 4):
    metrics.record("latency_ms", latency)
assert metrics.summary("latency_ms").count == 3
print(metrics.health("latency_ms", maximum=3))
```

## Test

```sh
python3 -m unittest tests.test_systems.MonitoringTests -v
python3 -m unittest discover -s tests -v
```

The full suite also includes release regression tests and executes these README examples.

## Complete and remaining

**Complete:** Window eviction, count/current/average/min/max and healthy/degraded/unknown outcomes.

**Remaining / limitations:** No live dashboard, exporter, alert delivery or persistence. Capacity is per metric; metric-name cardinality is unbounded. No load-test or non-finite-value guarantee.

## Learning takeaway

Bounding samples is different from bounding total cardinality; both matter for a real monitoring service.

## Command-line demonstration
Run a local telemetry demonstration. Values are explicitly simulated:

```bash
python3 -m projects.monitoring_dashboard latency_ms 112 128 146 121 --threshold 130 --capacity 4
```
