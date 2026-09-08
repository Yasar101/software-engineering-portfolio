# Worker Lease Scheduler Core

**TESTED CORE** · [Portfolio](../../README.md) · [Architecture](../../docs/ARCHITECTURE.md)

An in-memory job scheduler modelling claims, expiring leases and bounded retries.

## Purpose and engineering skills

Explore ownership, worker failure and terminal-state behavior before choosing a queue or database.

## Structure

scheduler.py uses immutable Job records, defensive payload copies and a process-local lock; the clock is injectable. [Source](scheduler.py).

## Run

From the repository root with Python 3.11+, run this offline example using `python3` (no dependencies or credentials):

```python
from projects.distributed_ai_platform import JobScheduler, JobState
scheduler = JobScheduler(max_attempts=2)
job = scheduler.submit({"model": "demo"})
claim = scheduler.claim("worker-instance-1", lease_seconds=30)
assert claim.id == job.id
assert scheduler.finish(job.id, "worker-instance-1", True).state == JobState.SUCCEEDED
```

## Test

```sh
python3 -m unittest tests.test_systems.SchedulerTests -v
python3 -m unittest discover -s tests -v
```

The full suite also includes release regression tests and executes these README examples.

## Complete and remaining

**Complete:** Submission, claim/finish, ownership and expiry checks, retry limits and exhausted-expiry transition to FAILED on get/claim. Tests use a deterministic clock.

**Remaining / limitations:** Single process only: no durable queue, network workers, fencing token, heartbeat or exactly-once delivery. Use a unique worker ID for each execution attempt; reused IDs cannot distinguish stale attempts. No AI inference engine is included.

## Learning takeaway

A lease needs expiry and exhaustion semantics; a process-local lock is not a distributed consistency mechanism.
