"""Tests for the health endpoint."""

from fastapi.testclient import TestClient

from app.main import app


def test_application_imports() -> None:
    """The FastAPI application exposes its configured metadata."""
    assert app.title == "Healthcare Operations API"
    assert app.version == "0.1.0"


def test_health_endpoint_returns_healthy_status() -> None:
    """The health endpoint confirms that the process is running."""
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
