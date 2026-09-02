# Healthcare Operations API

An educational, portfolio-grade backend application for demonstrating professional healthcare-operations engineering practices. The repository uses synthetic data only and is intended to remain understandable, maintainable, and explainable by an early-career backend engineer.

> This is not a production medical system. It does not use real patient data or PHI, and it does not claim HIPAA compliance or regulatory certification.

## Current Status

Milestone 1 establishes a runnable FastAPI project foundation. It currently provides typed application settings, minimal standard-library logging, and a process health endpoint. No database, authentication, authorization, domain models, scheduling, Docker, CI, or cloud infrastructure has been implemented.

## Technology Stack

- Python 3.12+
- FastAPI and Uvicorn
- Pydantic and pydantic-settings
- uv for dependency management
- pytest and HTTPX for testing
- Ruff for formatting and linting

## Architecture

The project is a modular monolith. Routes remain thin, with future business rules planned for services and database access planned for repositories. Typed configuration lives in `app/core/`. See [Architecture](docs/architecture.md) for implemented and planned boundaries.

## Requirements

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/)

## Setup

```text
uv sync
```

Optionally copy `.env.example` to `.env` and adjust non-secret local settings. Do not commit `.env`.

## Run Locally

```text
uv run uvicorn app.main:app --reload
```

The API runs at `http://127.0.0.1:8000`. Interactive OpenAPI documentation is available at `http://127.0.0.1:8000/docs` while the server is running.

## Testing and Quality Checks

```text
uv run pytest
uv run ruff format --check .
uv run ruff check .
```

To apply Ruff formatting locally, run `uv run ruff format .` and then rerun the checks.

## Endpoint

| Method | Path | Response |
| --- | --- | --- |
| `GET` | `/health` | `200 OK` with `{"status":"healthy"}` |

`GET /health` confirms only that the application process is running. It does not check database or external-service readiness.

## Roadmap

1. Project foundation: FastAPI setup, settings, health check, testing, and code quality tooling.
2. Persistence and migrations: PostgreSQL, SQLAlchemy, and Alembic.
3. Domain workflows: approved synthetic healthcare operations entities and rules.
4. Authentication, authorization, and minimal audit events.
5. Containerization and continuous integration.

Future work is introduced only through approved milestones.

## Security and Privacy

Use synthetic/demo data only. Never commit credentials, tokens, private keys, `.env` files, database dumps, or sensitive-like records. Logs must not include secrets, complete notes, complete form responses, or full patient records.

## License

No license has been selected yet.
