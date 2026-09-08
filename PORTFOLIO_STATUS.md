# Portfolio status

Reviewed 2026-09-08. This is an employer-facing reference portfolio, not a production deployment claim.

## Validation

- Python 3.13.13: `python3 -m compileall -q projects` passed.
- `python3 -m unittest discover -s tests -v`: **29 tests passed**, including eleven new failure-path regressions and two documentation checks.
- All ten project README Python examples execute offline. Relative Markdown targets and anchors pass validation.
- Public profile, Actions page and badge links returned HTTP 200 during review.
- Tracked/proposed content, file sizes, sensitive filenames and credential patterns were reviewed; only regex source and explicit dummy test inputs matched. No unresolved detected secrets or unintended data artifacts.
- CI configuration: Python 3.11/3.12/3.13 matrix, compile and full test commands, read-only contents permissions and five-minute job timeout. Local results do not assert a remote CI result: [inspect current Actions runs](https://github.com/Yasar101/software-engineering-portfolio/actions/workflows/ci.yml).

## Implemented scope

| Project | Status | Remaining boundary |
| --- | --- | --- |
| CLI Calculator | TESTED | Small expression grammar only |
| Expense Tracker | TESTED | Local JSON; no multi-writer or recovery guarantees |
| Weather Core | TESTED CORE | HTTP function exists; live API and dashboard UI unverified/unimplemented |
| Task Manager | TESTED | SQLite repository; no web interface or authentication |
| Energy Calculator | TESTED | Estimates from caller-provided inputs; no live tariffs |
| REST / PostgreSQL | REFERENCE IMPLEMENTATION | No HTTP server or PostgreSQL adapter; illustrative schema |
| Monitoring Core | TESTED CORE | Per-metric history; no dashboard/exporter/load testing |
| Commerce Core | TESTED CORE | In-process compensation; no durable payment transaction |
| AI Assistant Core | TESTED CORE | Fake provider tests; no model-quality or comprehensive safety evidence |
| Scheduler Core | TESTED CORE | Single-process memory; no persistence or fencing token |

See each project README for its working example and limitations. No unreviewed supporting repository is promoted as validated work.
