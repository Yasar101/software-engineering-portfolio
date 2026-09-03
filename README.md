# Software Engineering Portfolio

[![CI](https://github.com/Yasar101/software-engineering-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/Yasar101/software-engineering-portfolio/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A tested progression from command-line fundamentals to service-oriented and distributed-system design. The portfolio prioritizes small, readable domain models, explicit boundaries, failure-path testing, and credential-safe configuration.

## At a glance

- Ten independently documented Python projects
- Sixteen automated tests covering principal success and failure paths
- CI compilation and tests on Python 3.11, 3.12, and 3.13
- Standard-library-first implementations that run without paid services
- Replaceable boundaries for databases, HTTP APIs, model providers, and workers

## Project progression

| Level | Project | Engineering focus | Status |
|---|---|---|---|
| Beginner | [CLI Calculator](projects/cli_calculator/) | Input validation, safe parsing, exact decimals | Tested |
| Beginner | [Expense Tracker](projects/expense_tracker/) | Data modelling, JSON persistence, reports | Tested |
| Beginner | [Weather Dashboard](projects/weather_dashboard/) | HTTP adapter, response validation, presentation model | Tested core |
| Intermediate | [Task Manager](projects/task_manager/) | SQLite repository, state transitions, filtering | Tested |
| Intermediate | [Energy Calculator Pro](projects/energy_calculator/) | Domain calculations, tariffs, emissions | Tested |
| Intermediate | [PostgreSQL REST API](projects/postgres_rest_api/) | REST semantics, repository port, SQL schema | Tested reference |
| Advanced | [Monitoring Dashboard](projects/monitoring_dashboard/) | Thread safety, bounded rolling windows, health | Tested core |
| Advanced | [Commerce Platform](projects/microservices_commerce/) | Service boundaries, reservation, compensation | Tested core |
| Advanced | [AI Developer Assistant](projects/ai_developer_assistant/) | Retrieval, bounded prompts, secret detection | Tested core |
| Advanced | [Distributed AI Platform](projects/distributed_ai_platform/) | Worker leases, ownership, retries, terminal states | Tested core |

“Core” and “reference” identify deliberately framework-neutral implementations. They demonstrate tested domain and integration boundaries without claiming a deployed production service.

## Featured engineering decisions

- The calculator never evaluates user input as code.
- Financial and energy calculations use `Decimal` instead of binary floating point.
- SQLite and JSON adapters make local persistence deterministic and easy to inspect.
- External weather calls are separated from parsing, allowing offline tests.
- The commerce workflow compensates inventory when payment fails.
- AI prompts reject likely credentials before invoking a provider.
- Distributed jobs use expiring leases and enforce worker ownership.

See [the architecture notes](docs/ARCHITECTURE.md) for the design progression and [the portfolio audit](PORTFOLIO_AUDIT.md) for evidence and limitations.

## Run locally

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

## Validate

```bash
python3 -m compileall -q projects
python3 -m unittest discover -s tests -v
```

CI repeats both checks for every push and pull request. Tests do not contact external services.

## Repository map

```text
projects/                Ten isolated application packages
tests/                   Unified unit and workflow tests
docs/                    Architecture and portfolio integration notes
.github/workflows/       Continuous integration
PORTFOLIO_AUDIT.md       Findings and evidence
PORTFOLIO_PLAN.md        Delivery and integration roadmap
PORTFOLIO_STATUS.md      Current validation status
```

## Related work

The following existing repositories are being evaluated as supporting evidence of earlier web and application-development work. They remain independent and are not renamed, deleted, or copied into this repository.

- [aston-fitness-project](https://github.com/Yasar101/aston-fitness-project)
- [BasicPHP1](https://github.com/Yasar101/BasicPHP1)
- [assignment2](https://github.com/Yasar101/assignment2)
- [my-first-website](https://github.com/Yasar101/my-first-website)
- [my-first-website1](https://github.com/Yasar101/my-first-website1)

Their promotion priority is documented in [the integration plan](docs/EXISTING_REPOSITORIES.md); no technology or quality claims are made until each repository can be inspected and validated.

## Security and licence

Copy `.env.example` to `.env` for local configuration and never commit credentials. Original code in this repository is available under the [MIT License](LICENSE). See [CONTRIBUTING.md](CONTRIBUTING.md) for the development workflow and [SECURITY.md](SECURITY.md) for responsible vulnerability reporting.
