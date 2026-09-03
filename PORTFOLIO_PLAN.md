# Portfolio Delivery Plan

## Strategy

Build one cohesive Python monorepo that demonstrates increasing engineering depth while keeping each project independently understandable. Shared conventions reduce maintenance, and isolated project packages make later repository extraction straightforward.

## Delivery sequence

1. Establish repository governance, CI, documentation, and test discovery.
2. Implement foundational applications: calculator, expense tracker, weather dashboard, task manager, and energy calculator.
3. Implement backend and systems applications: REST API, monitoring dashboard, commerce services, AI developer assistant, and distributed AI job platform.
4. Run compile checks and the full test suite; fix failures before changing status.
5. Commit coherent milestones and update `PORTFOLIO_STATUS.md` with evidence.
6. Audit GitHub repositories and decide which projects should become standalone repositories after authentication is restored.

## Definition of done

A project is complete when its core use case is implemented, its public behavior is documented, automated tests cover principal success and failure paths, and the project passes the repository-wide validation command. Integrations that require credentials must have safe configuration examples and mocked tests.

## Architecture decisions

- Python 3.11+ provides a consistent learning progression across projects.
- SQLite is used for local persistence and deterministic testing; the PostgreSQL project exposes repository boundaries suitable for a production driver.
- Network-facing components separate transport code from domain logic.
- Advanced projects are small reference implementations, not claims of production-scale infrastructure.

