# Architecture

The portfolio is a modular monorepo. Each numbered directory is a Python package with a narrow domain boundary. Tests import packages through the repository root, so no installation step is required for development.

The first five projects emphasize correctness and local application design. Projects six through ten demonstrate ports-and-adapters boundaries: domain logic does not depend on HTTP servers, databases, model vendors, or worker processes. Those adapters can therefore be replaced without changing the tested core.

The CI workflow performs syntax compilation and discovers all unit tests on supported Python versions. External APIs are never called by tests.

