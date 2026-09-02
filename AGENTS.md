# Repository Guidelines

## Purpose and Scope

Healthcare Operations API is educational, portfolio-grade backend software. It demonstrates professional engineering practices while remaining understandable and defensible by an early-career developer. It uses synthetic healthcare operations data only; it is not production software and must never claim HIPAA compliance or regulatory certification.

Build incrementally through reviewed milestones. Implement only the requested milestone and do not add future domain functionality early. Prefer correctness, security, maintainability, readability, and testability over unnecessary complexity or technology breadth.

## Approved V1 Architecture

Use Python 3.12+, FastAPI, PostgreSQL, SQLAlchemy 2.x, Alembic, Pydantic with `pydantic-settings`, pytest, Docker Compose, GitHub Actions, uv, and Ruff. The application is a modular monolith.

Keep routes thin: routes handle HTTP concerns, schemas define request/response contracts, services enforce business and application rules, repositories own database queries, and models represent persistence. Centralize authentication and authorization in policies/dependencies and configuration in a typed settings module. Avoid generic repository frameworks, complex dependency-injection frameworks, and abstraction without a concrete need.

When introduced, organize code under `app/` by responsibility, such as `app/api/`, `app/services/`, `app/repositories/`, `app/schemas/`, `app/models/`, `app/policies/`, and `app/core/`. Mirror application areas under `tests/`. Keep Alembic, Docker, and CI configuration in conventional root-level locations. Document only files and commands that exist.

## Engineering Practices

Use four-space Python indentation, complete type hints for public interfaces, `snake_case` for modules/functions/fields, and `PascalCase` for classes and Pydantic/SQLAlchemy models. Prefer small, descriptive functions and straightforward control flow. Explain non-obvious architectural decisions in code comments or documentation.

Validate API input with Pydantic, return predictable errors without internal details, and enforce important business rules in services. Add database constraints for final integrity when appropriate. Use async only when it provides a clear benefit, and apply it consistently within a workflow. Keep dependencies minimal.

Do not assume application-level pre-checks alone preserve integrity under concurrent requests. For race-prone operations, use appropriate transactions and database constraints where practical, test concurrent behavior when meaningful, and explicitly document known V1 limitations.

Handle expected domain errors explicitly; never silently swallow unexpected exceptions. Log unexpected failures safely and return sanitized server errors without stack traces, secrets, credentials, tokens, database implementation details, or sensitive-like record contents.

Appointment-overlap prevention belongs in V1. Patient deletion must soft-archive records. Minimal audit events belong in V1 but must not include sensitive record bodies. JWT access and refresh tokens are future authentication work, not part of the project-foundation milestone.

Planned V1 domain areas are users, providers, synthetic patients, appointments, operational tasks, internal notes, form templates/submissions, and minimal audit events. Implement an area only in its assigned milestone.

Do not introduce microservices, Redis, Kafka, Celery, Kubernetes, message brokers, distributed tracing, multi-tenancy, external identity providers, a frontend, cloud infrastructure, Terraform, AWS CDK, cloud SDKs, complex scheduling, or file uploads unless a later milestone explicitly approves them.

## Security and Privacy

Never use real patient data, PHI, employer/client data, proprietary code, or production database dumps. Never commit `.env` files, credentials, passwords, tokens, API/private keys, or sensitive data. Keep `.env` ignored and put placeholders only in `.env.example`.

Do not log passwords, bearer tokens, complete notes, form responses, or full patient records; redact sensitive-like values where appropriate. Apply least-privilege authorization. Tests and local fixtures must use synthetic data only and must not call external production services.

## Tests and Quality Checks

Every meaningful feature needs deterministic tests. Use unit tests for isolated business logic, integration tests for database behavior, and API tests for HTTP contracts, validation, authorization, and important workflows. Name files `test_<area>.py` and tests `test_<expected_behavior>`.

Before proposing a commit, when applicable: run Ruff formatting checks and linting, run relevant pytest tests, review `git diff`, check for accidental secrets or sensitive data, and confirm documentation matches the implementation. Report failures and warnings; do not knowingly commit failing tests.

## Git, Documentation, and Milestones

Do not commit directly to `main`. Use focused feature branches, logically scoped commits, and professional imperative messages, for example `Add appointment overlap validation`. Before committing, report the proposed commit message. Never push, merge, delete branches, rewrite history, force-push, or modify repository settings without explicit approval.

For each milestone: inspect the repository, confirm scope, implement only that scope, validate it, summarize changes and results, report unresolved issues, propose a commit message, then stop for approval before committing or pushing. Keep README/setup instructions reproducible and factual; clearly label planned functionality. Optimize every change for clean architecture, meaningful tests, sensible Git history, security awareness, and interview-ready explanations.
