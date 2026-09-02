"""Application health endpoint."""

from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    """Response returned when the application process is available."""

    status: Literal["healthy"]


@router.get("/health", response_model=HealthResponse, summary="Check application health")
def get_health() -> HealthResponse:
    """Confirm that the application process is running.

    This endpoint does not verify database or external-service readiness.
    """
    return HealthResponse(status="healthy")
