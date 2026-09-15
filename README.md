# YASAR — Software Systems Engineering

[![CI](https://github.com/Yasar101/software-engineering-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/Yasar101/software-engineering-portfolio/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Yasar Ashraf · Building from programming fundamentals toward backend systems and software architecture.**

A working, static portfolio presentation accompanies the tested code, with **15 projects** — 10 Python software/systems cores plus 5 web foundations and PHP projects. Every project links to its public source and to an **offline, browser-rendered demo** (live page, interactive simulation, animated visualization, or architecture walk-through) with no external services and no third-party dependencies.

## View the portfolio

- **Live:** <https://yasar101.github.io/software-engineering-portfolio/>
- **Local:** open [`index.html`](index.html) directly, or serve it with `python3 -m http.server 8000`.

Edit [`portfolio-data.js`](portfolio-data.js) to update project copy, links, classifications, or contact details. The site includes project-discipline filtering, a persisted light/dark theme, copyable demonstration commands, interactive demos, and explicit limitations. It has no analytics, forms, or third-party dependencies.

The Python projects are 3.11+ standard-library-only implementations with explicit boundaries; the systems and AI projects are tested reference cores, not deployed platforms.

## Start here

- **Backend:** inspect the [SQLite Task Manager](projects/task_manager/) for persistence and parameterized SQL, then the [REST service reference](projects/postgres_rest_api/) for validation and repository boundaries.
- **Systems:** compare [commerce compensation](projects/microservices_commerce/) with [worker leases and retries](projects/distributed_ai_platform/).
- **AI / automation:** inspect the [assistant core](projects/ai_developer_assistant/) for context selection, a provider contract and the limits of regex-based screening.
- **Architecture:** read the [design overview](docs/ARCHITECTURE.md). [Validation status](PORTFOLIO_STATUS.md) and the [release audit](PORTFOLIO_AUDIT.md) separate evidence from remaining work.

## Featured projects

| Project | Evidence to inspect | Boundary |
| --- | --- | --- |
| [REST / PostgreSQL Reference](https://github.com/Yasar101/postgresql-rest-api) · [demo](demos/rest-api.html) | Validation status/body pairs and repository Protocol | In-memory adapter; no running PostgreSQL server |
| [Commerce Workflow](https://github.com/Yasar101/microservices-commerce-platform) · [demo](demos/commerce.html) | Inventory compensation on payment rejection and exceptions | In-process model; no durable saga or payment integration |
| [Worker Lease Scheduler](https://github.com/Yasar101/distributed-ai-systems-platform) · [demo](demos/scheduler.html) | Ownership, expired attempts, retry limits, defensive state copies | Single-process reference; no distributed deployment |
| [AI Developer Assistant](https://github.com/Yasar101/ai-developer-assistant) · [demo](demos/assistant.html) | Offline retrieval/provider tests; context screening and size limits | Keyword retrieval and fake provider; no model-quality claim |
| [Fitness Tracking Web App](https://github.com/Yasar101/fitness-tracking-web-app) · [demo](demos/fitness-tracker/index.html) | Semantic HTML, responsive layout, client validation | Static front-end; no backend or persistence |

The repository also includes a static portfolio site, CI compilation/tests on Python 3.11–3.13, and standard-library-first implementations with replaceable database, HTTP, model-provider, and worker boundaries.

## Project progression and honest demo status

| Focus | Project | Evidence | Status | Demo |
| --- | --- | --- | --- | --- |
| Fundamentals | [CLI Calculator](https://github.com/Yasar101/python-cli-calculator) | Explicit parsing, Decimal, error handling | TESTED | [demo](demos/calculator.html) |
| Data modelling | [Expense Tracker](https://github.com/Yasar101/personal-expense-tracker) | JSON round trips and category/monthly totals | TESTED | [demo](demos/expense-tracker.html) |
| API integration boundary | [Weather Core](https://github.com/Yasar101/weather-dashboard) | Response parsing and offline fixture tests | TESTED CORE | [demo](demos/weather-dashboard.html) |
| Databases | [Task Manager](https://github.com/Yasar101/task-manager-application) | SQLite repository and state transitions | TESTED | [demo](demos/task-manager.html) |
| Domain modelling | [Energy Calculator](https://github.com/Yasar101/energy-calculator-pro) | Units, Decimal and rounding | TESTED | [demo](demos/energy-calculator.html) |
| Backend architecture | [REST / PostgreSQL Reference](https://github.com/Yasar101/postgresql-rest-api) | Repository protocol and HTTP-style response semantics | REFERENCE IMPLEMENTATION | [demo](demos/rest-api.html) |
| Systems | [Monitoring Core](https://github.com/Yasar101/real-time-monitoring-dashboard) | Locked per-metric rolling windows | TESTED CORE | [demo](demos/monitoring-dashboard.html) |
| Failure handling | [Commerce Workflow](https://github.com/Yasar101/microservices-commerce-platform) | Reservation and compensation | TESTED CORE | [demo](demos/commerce.html) |
| AI engineering | [Developer Assistant](https://github.com/Yasar101/ai-developer-assistant) | Retrieval, prompt construction, provider injection | TESTED CORE | [demo](demos/assistant.html) |
| Distributed-systems concepts | [Lease Scheduler](https://github.com/Yasar101/distributed-ai-systems-platform) | Worker claims, leases and bounded retries | TESTED CORE | [demo](demos/scheduler.html) |
| Front-end web | [HTML & CSS Foundations](https://github.com/Yasar101/html-css-foundations) | Semantic markup and accessible base styling | TESTED PAGE | [demo](demos/html-css-foundations/index.html) |
| Front-end web | [Responsive Web Foundations](https://github.com/Yasar101/responsive-web-foundations) | Responsive layout and interaction patterns | TESTED PAGE | [demo](demos/responsive-web-foundations/index.html) |
| Server-side web | [PHP Calculator Fundamentals](https://github.com/Yasar101/php-calculator-fundamentals) | PHP operator logic and input validation | TESTED LOGIC | [demo](demos/php-calculator.html) |
| Full-stack web | [Fitness Tracking Web App](https://github.com/Yasar101/fitness-tracking-web-app) | Semantic HTML, responsive design, client validation | TESTED PAGE | [demo](demos/fitness-tracker/index.html) |
| Full-stack web | [PHP Project Management System](https://github.com/Yasar101/php-project-management-system) | Workflow, roles and module boundaries | ARCHITECTURE REVIEW | [demo](demos/project-manager.html) |

Every project is also presented in the static site with an engineering focus and an interactive or simulated demo; source and demo links are read from [`portfolio-data.js`](portfolio-data.js).

**TESTED** means the documented local behavior has automated checks, not that every input is covered. **TESTED CORE** identifies implemented logic without a complete deployed application. **REFERENCE IMPLEMENTATION** identifies a tested service contract with missing real adapters; the PostgreSQL schema is illustrative and has not been exercised against a PostgreSQL server. **TESTED PAGE / TESTED LOGIC** means the page or logic renders/behaves as demonstrated offline; the web projects' original servers (PHP, backend) are not deployed here.

## Demos

Each of the 15 projects links to an offline demo under [`demos/`](demos/):

- **Interactive demos** (calculator, expense tracker, task manager, energy calculator, REST console, PHP calculator) run entirely in the browser with seeded, clearly labelled data.
- **Simulations** (weather, assistant, scheduler) animate deterministic flows instead of calling real providers or external APIs.
- **Animated / architecture demos** (monitoring dashboard, commerce, project manager) visualize system behavior with explicit threshold and boundary labels.
- **Copies of the original static pages** (HTML & CSS foundations, responsive foundations, fitness tracker) are served from this site for review.

Demos are validated by `tests/test_demos.py` to stay offline (only `github.com` source links and localhost are allowed), reference existing files, and pass `node --check`.

## Run and test

```bash
git clone https://github.com/Yasar101/software-engineering-portfolio.git
cd software-engineering-portfolio
python3 -m unittest discover -s tests -v
```

Python 3.11 or newer is recommended. The projects currently use the standard library, so no dependency installation is required.

Run the calculator directly:

```bash
python3 -m projects.cli_calculator.calculator "12.5 * 4"
```

## Run local project demonstrations

`demo.py` is a dependency-free command-line presentation layer over the real
project code. It uses clearly labelled seeded data and never calls external
providers. For example:

```bash
python3 demo.py expenses
python3 demo.py energy --watts 850 --hours 3.5 --days 30 --tariff 0.28
python3 demo.py commerce --fail-payment
python3 demo.py assistant
python3 demo.py scheduler
```

Run `python3 demo.py --help` for every available project demonstration.

## Validate

```bash
python3 -m compileall -q projects
python3 -m unittest discover -s tests -v
```

The suite currently has **36 tests**, including failure-path regressions, relative-link and demo validation (offline-only URLs, file existence, JavaScript syntax) and execution of all project README examples. Tests need no credentials or external services. Each project README provides a short offline Python example and a focused test command.

For a CLI example:

```sh
python3 -m projects.cli_calculator.calculator "12.5 * 4"
```

CI runs compilation and tests on Python 3.11, 3.12 and 3.13 for pushes and pull requests. The Actions badge links to the current remote result; local validation is recorded separately in [PORTFOLIO_STATUS.md](PORTFOLIO_STATUS.md).

## Engineering approach
```text
projects/                Ten isolated application packages
tests/                   Unified unit and workflow tests
demos/                   Offline browser demos for all 15 public projects
docs/                    Architecture and portfolio integration notes
.github/workflows/       Continuous integration + Pages deploy
index.html               Static portfolio presentation
portfolio-data.js        Central presentation content/configuration
styles.css, script.js    Responsive design system and interactions
demo.css, demo.js        Shared mock-header chrome for offline demos
PORTFOLIO_AUDIT.md       Findings and evidence
PORTFOLIO_PLAN.md        Delivery and integration roadmap
PORTFOLIO_STATUS.md      Current validation status
```

## Related work awaiting source verification

The following owner-approved repositories may become supporting evidence of earlier web and application-development work. Their source and live deployments have not been verified in this environment, so they are not represented as live portfolio demonstrations. They remain independent and are not renamed, deleted, or copied into this repository.

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
