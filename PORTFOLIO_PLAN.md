# Portfolio Delivery Plan

## Strategy

Build one cohesive Python monorepo that demonstrates increasing engineering depth while keeping each project independently understandable. Shared conventions reduce maintenance, and isolated project packages make later repository extraction straightforward.

## Delivery sequence

1. Establish repository governance, CI, documentation, and test discovery.
2. Implement foundational applications: calculator, expense tracker, weather dashboard, task manager, and energy calculator.
3. Implement backend and systems applications: REST API, monitoring dashboard, commerce services, AI developer assistant, and distributed AI job platform.
4. Run compile checks and the full test suite; fix failures before changing status.
5. Commit coherent milestones and update `PORTFOLIO_STATUS.md` with evidence.
6. Audit the five owner-approved GitHub repositories and classify them against the promotion gate after authenticated network access is restored.
7. Improve qualifying repositories independently, preserving their names, visibility, and history.
8. Promote only validated work in the central README and GitHub profile pins.

## Definition of done

A project is complete when its core use case is implemented, its public behavior is documented, automated tests cover principal success and failure paths, and the project passes the repository-wide validation command. Integrations that require credentials must have safe configuration examples and mocked tests.

## Architecture decisions

- Python 3.11+ provides a consistent learning progression across projects.
- SQLite is used for local persistence and deterministic testing; the PostgreSQL project exposes repository boundaries suitable for a production driver.
- Network-facing components separate transport code from domain logic.
- Advanced projects are small reference implementations, not claims of production-scale infrastructure.

## Existing repository integration

Detailed criteria and sequencing are maintained in `docs/EXISTING_REPOSITORIES.md`.

1. Inspect and validate `aston-fitness-project` first as the strongest provisional case-study candidate.
2. Review `BasicPHP1` for safe server-side implementation and evidence of language breadth.
3. Compare `my-first-website` with `my-first-website1`; feature at most one unless their differences tell a clear progression story.
4. Review `assignment2` for attribution and original contribution before including it beyond learning history.
5. Add accurate descriptions, topics, screenshots, CI, and profile pins only after content-based validation and with no visibility changes.

## Next implementation milestones

- Restore read-only GitHub access and complete the five source-level audits.
- Convert the PostgreSQL reference boundary into a tested live adapter using an ephemeral CI service.
- Add transport adapters or small demos for the weather, monitoring, and distributed-system cores.
- Add coverage reporting and static analysis once they provide useful signal without obscuring the dependency-light setup.
