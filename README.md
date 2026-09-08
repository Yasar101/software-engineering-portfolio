# Software Engineering Portfolio

[![CI](https://github.com/Yasar101/software-engineering-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/Yasar101/software-engineering-portfolio/actions/workflows/ci.yml)

**Yasar Ashraf · Building from programming fundamentals toward backend systems and software architecture.**

Ten small Python projects make that progression inspectable through source, offline examples, tests and explicit limitations. The systems and AI projects are tested reference cores, not deployed platforms. Python 3.11+; standard library only.

## Start here

- **Backend:** inspect the [SQLite Task Manager](projects/task_manager/) for persistence and parameterized SQL, then the [REST service reference](projects/postgres_rest_api/) for validation and repository boundaries.
- **Systems:** compare [commerce compensation](projects/microservices_commerce/) with [worker leases and retries](projects/distributed_ai_platform/).
- **AI / automation:** inspect the [assistant core](projects/ai_developer_assistant/) for context selection, a provider contract and the limits of regex-based screening.
- **Architecture:** read the [design overview](docs/ARCHITECTURE.md). [Validation status](PORTFOLIO_STATUS.md) and the [release audit](PORTFOLIO_AUDIT.md) separate evidence from remaining work.

## Featured projects

| Project | Evidence to inspect | Boundary |
| --- | --- | --- |
| [SQLite Task Manager](projects/task_manager/) | Parameterized queries, committed state changes, workflow tests | Local repository; no web app or authentication |
| [Commerce Workflow](projects/microservices_commerce/) | Inventory compensation on payment rejection and exceptions | In-process model; no durable saga or payment integration |
| [Worker Lease Scheduler](projects/distributed_ai_platform/) | Ownership, expired attempts, retry limits, defensive state copies | Single-process reference; no distributed deployment |
| [AI Developer Assistant](projects/ai_developer_assistant/) | Offline retrieval/provider tests; context screening and size limits | Keyword retrieval and fake provider; no model-quality claim |

## Project progression

| Focus | Project | Evidence | Status |
| --- | --- | --- | --- |
| Fundamentals | [CLI Calculator](projects/cli_calculator/) | Explicit parsing, Decimal, error handling | TESTED |
| Data modelling | [Expense Tracker](projects/expense_tracker/) | JSON round trips and category/monthly totals | TESTED |
| API integration boundary | [Weather Core](projects/weather_dashboard/) | Response parsing and offline fixture tests | TESTED CORE |
| Databases | [Task Manager](projects/task_manager/) | SQLite repository and state transitions | TESTED |
| Domain modelling | [Energy Calculator](projects/energy_calculator/) | Units, Decimal and rounding | TESTED |
| Backend architecture | [REST / PostgreSQL Reference](projects/postgres_rest_api/) | Repository protocol and HTTP-style response semantics | REFERENCE IMPLEMENTATION |
| Systems | [Monitoring Core](projects/monitoring_dashboard/) | Locked per-metric rolling windows | TESTED CORE |
| Failure handling | [Commerce Workflow](projects/microservices_commerce/) | Reservation and compensation | TESTED CORE |
| AI engineering | [Developer Assistant](projects/ai_developer_assistant/) | Retrieval, prompt construction, provider injection | TESTED CORE |
| Distributed-systems concepts | [Lease Scheduler](projects/distributed_ai_platform/) | Worker claims, leases and bounded retries | TESTED CORE |

**TESTED** means the documented local behavior has automated checks, not that every input is covered. **TESTED CORE** identifies implemented logic without a complete deployed application. **REFERENCE IMPLEMENTATION** identifies a tested service contract with missing real adapters; the PostgreSQL schema is illustrative and has not been exercised against a PostgreSQL server.

## Run and test

```sh
git clone https://github.com/Yasar101/software-engineering-portfolio.git
cd software-engineering-portfolio
python3 -m compileall -q projects
python3 -m unittest discover -s tests -v
```

The suite currently has **29 tests**, including failure-path regressions, relative-link validation and execution of all ten project README examples. Tests need no credentials or external services. Each project README provides a short offline Python example and a focused test command.

For a CLI example:

```sh
python3 -m projects.cli_calculator.calculator "12.5 * 4"
```

CI runs compilation and tests on Python 3.11, 3.12 and 3.13 for pushes and pull requests. The Actions badge links to the current remote result; local validation is recorded separately in [PORTFOLIO_STATUS.md](PORTFOLIO_STATUS.md).

## Engineering approach

Keep behavior small enough to understand, make state ownership explicit, and test failures before presenting reliability claims. Progression here means increasing design depth, not production scale or a claim of seniority. The [architecture notes](docs/ARCHITECTURE.md) explain both design choices and trade-offs.

## Repository guide

- [projects/](projects/) — independent packages and concise project guides.
- [tests/](tests/) — unit, workflow, regression and documentation checks.
- [PORTFOLIO_AUDIT.md](PORTFOLIO_AUDIT.md) — findings, fixes and evidence limits.
- [PORTFOLIO_PLAN.md](PORTFOLIO_PLAN.md) — future milestones, separate from delivered work.
- [CONTRIBUTING.md](CONTRIBUTING.md) · [SECURITY.md](SECURITY.md) · [MIT license](LICENSE).
- [Earlier repository review policy](docs/EXISTING_REPOSITORIES.md) — supporting work is not featured until its source and run path are validated.
- [GitHub profile](https://github.com/Yasar101/Yasar101).

No environment file is needed for the current examples. Never include personal data, credentials or generated local databases in a contribution.
