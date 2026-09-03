# Software Engineering Portfolio

A progressive collection of ten Python projects, from command-line fundamentals to distributed AI system design. Every project is designed to run locally without paid services or committed credentials.

## Projects

| Level | Project | Demonstrates |
|---|---|---|
| Beginner | `projects/cli_calculator` | Parsing, decimal arithmetic, CLI design |
| Beginner | `projects/expense_tracker` | Data modelling, persistence, reporting |
| Beginner | `projects/weather_dashboard` | HTTP clients, validation, presentation |
| Intermediate | `projects/task_manager` | SQLite, state transitions, filtering |
| Intermediate | `projects/energy_calculator` | Domain calculations, tariffs, emissions |
| Intermediate | `projects/postgres_rest_api` | REST semantics, repositories, SQL boundaries |
| Advanced | `projects/monitoring_dashboard` | Metrics, rolling windows, health status |
| Advanced | `projects/microservices_commerce` | Service boundaries, inventory, order workflows |
| Advanced | `projects/ai_developer_assistant` | Context retrieval, prompt construction, safety |
| Advanced | `projects/distributed_ai_platform` | Scheduling, leases, retries, worker coordination |

## Validate

```bash
python3 -m compileall -q projects
python3 -m unittest discover -s tests -v
```

Python 3.11 or newer is recommended. Individual project READMEs include focused examples.

## Repository layout

Application packages live under `projects/`; the root `tests/` directory provides unified validation. Architectural notes live under `docs/`.
