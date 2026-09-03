# Contributing

This portfolio favors small, reviewable changes with tests that explain behavior.

## Development workflow

1. Create a focused branch from `main`.
2. Keep project domain logic isolated from external services.
3. Add or update tests for changed behavior.
4. Run the validation commands below.
5. Open a pull request describing the problem, approach, and test evidence.

```bash
python3 -m compileall -q projects
python3 -m unittest discover -s tests -v
```

Do not commit `.env` files, credentials, local databases, generated output, or unrelated formatting changes.

