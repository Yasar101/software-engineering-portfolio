# Portfolio roadmap

[Portfolio](README.md) · [Current evidence](PORTFOLIO_STATUS.md)

## Delivered

Ten documented Python implementations, offline examples, Git history, CI and release regression checks. The current release distinguishes tested local behavior from incomplete integrations. See PORTFOLIO_AUDIT.md for concrete fixes.

## Next milestones — not completed claims

1. Validate a real PostgreSQL adapter against an ephemeral database, preserving the repository contract. Add HTTP transport only with request/response integration tests.
2. Choose one systems core for a durable-state milestone: define concurrency, restart and idempotency requirements before adding infrastructure.
3. Evaluate the AI assistant with a consented synthetic dataset and a real provider; assess answer quality and data handling independently from unit tests.
4. Add a small UI or transport demo where it materially improves inspection; do not rename a tested core as a deployed platform.
5. Promote independently completed projects only when their source, tests, contribution boundaries and public availability can be verified.

Work one milestone at a time. Coverage tools, additional linters and dependency upgrades are optional follow-ups, not substitutes for meaningful behavior tests.

## Release gate

Compilation and all tests pass; examples run; links and claims match source; staged changes are reviewed for secrets/private data and accidental artifacts; public history is preserved. A reference release can be ready for employers while deployment integrations remain explicitly unimplemented.
