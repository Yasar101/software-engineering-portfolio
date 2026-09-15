# Employer-facing release audit

Audit date: 2026-09-08. Baseline: `142d697` on main. Prior audits remain in Git history; the findings below describe the current review.

## Outcome

Ten small implementations now have concise, executable documentation and explicit maturity labels. The release demonstrates programming, persistence, service contracts, tests, CI and systems/AI design boundaries without claiming real distributed infrastructure, a PostgreSQL deployment or a production AI agent.

## Findings and changes

| Finding | Change | Evidence |
| --- | --- | --- |
| Per-project guides were mostly one paragraph | Added purpose, structure, offline example, focused tests, completed behavior, limits and a learning takeaway | All ten examples execute in test_documentation.py |
| Navigation did not identify strongest inspectable work | Featured task persistence, commerce failure handling, worker leases and provider-boundary tests | Source-linked root table and architecture overview |
| Audit/status files contained obsolete access blockers and stale latest-commit claims | Replaced with dated local evidence and live Actions navigation | PORTFOLIO_STATUS.md |
| Payment exceptions leaked reservations | Restore inventory and propagate the exception; document unknown payment outcome | test_payment_exception_releases_reservation |
| Expired workers could finish; exhausted expiry could strand RUNNING jobs | Check expiry at finish and terminalize exhausted leases on inspection/claim | Expired-worker and final-attempt regressions |
| Invalid lease/retry settings and shared payload mutation | Validate finite positive leases/integer retry budget; copy payload snapshots | Configuration and mutation regressions |
| Assistant screened only the question and left its size unbounded | Screen selected context/path, support quoted assignments, cap question/path sizes | Provider-not-called and length regressions |
| Item service converted invalid name types to strings | Reject non-string names | API validation regression |
| Calculator accepted non-finite operands | Reject NaN/Infinity before arithmetic | Finite-operand regression |
| Environment template implied configuration the code never read | State that current examples need no environment file | .env.example and root instructions |

Eleven new regression tests reproduced the defects before the changes. The original 16 tests remain; two documentation tests bring the suite to 29. One initial regression invocation was made outside the repository root and failed discovery; the recorded behavior failures and final passing results used the documented repository-root command.

## Presentation and demo audit (2026-09-15)

All 15 public repositories are now featured with direct source links and offline demos under `demos/`. The demos are validated to make no external calls other than `github.com` source links, to exist for every featured project, and to pass `node --check` (`tests/test_demos.py`). Web/PHP projects render their original static pages or a clearly labelled simulation; no PHP/backend runtime is deployed and no private repository name appears in tracked files.

## Release evidence

Compilation, all 36 tests, all ten offline examples, relative links and `git diff --check` pass on Python 3.13.13. Public Markdown links returned HTTP 200. CI uses the same compile/test commands on Python 3.11–3.13; its remote result is available through Actions and is not inferred from local tests.

Before publication, proposed files were reviewed for environment files, credentials, key/token patterns, personal data, databases, runtime artifacts, symlinks and oversized files. Four pattern matches were regex source or clearly synthetic negative-test values; none was an unresolved credential. No non-example .env or private-key filenames were found in repository history. A bounded scan is not an exhaustive guarantee about all possible secrets.

The original histories and repository visibility are preserved. Only the two authorized existing employer repositories are publication targets. New public repositories, private source and unrelated projects are outside this release.

## Employer review

| Reader | Two-minute inspection route | Honest boundary |
| --- | --- | --- |
| Junior software engineer employer | Calculator, expense model, run/test commands | Small comprehensible programs rather than claims of seniority |
| Backend employer | TaskManager SQL and REST service tests | Actual SQLite; PostgreSQL and HTTP adapters remain absent |
| Systems employer | Commerce compensation, scheduler expiry and architecture notes | Process-local models; no durable distributed deployment |
| AI / automation employer | Assistant retrieval and fake-provider failure tests | No live-model quality evaluation or autonomous agent |

## Remaining work

Future adapters and product-level interfaces are documented in PORTFOLIO_PLAN.md. Known reference limitations include scheduler fencing and durability, commerce idempotency and payment reconciliation, metrics cardinality, expense-file recovery, and heuristic AI screening. These are visible scope limits, not hidden passing-test claims. The featured web/PHP repositories show their original static pages or a clearly labelled architecture simulation; their original servers are not deployed and no other earlier repository is featured from its name alone.
