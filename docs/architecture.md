# Architecture

## Implemented Now

The project is a minimal FastAPI application organized as a modular-monolith foundation. `app/main.py` creates the application from typed settings in `app/core/config.py` and registers the health route in `app/api/health.py`.

`GET /health` confirms only that the application process is running. It has no database, external-service, authentication, or authorization readiness checks. Logging uses the Python standard library and a configurable, non-secret log level.

## Planned for Later Milestones

Later approved milestones may add PostgreSQL, SQLAlchemy, Alembic, domain models, repositories, services, request/response schemas, authentication, authorization, and domain workflows. Those components are intentionally absent from this foundation.

The intended design keeps API routes thin, business rules in services, persistence logic in repositories, database representation in models, and configuration in typed settings. Future concurrency-sensitive operations will use transactions and database constraints where practical.

This is educational portfolio software using synthetic data only. It is not a production medical system and does not claim HIPAA compliance or regulatory certification.
