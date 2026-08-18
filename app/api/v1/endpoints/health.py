from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.v1.schemas.health import HealthResponse
from app.application.health.use_cases import GetHealthStatus, get_health_status_use_case

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health_check(
    use_case: Annotated[GetHealthStatus, Depends(get_health_status_use_case)],
) -> HealthResponse:
    status = use_case.execute()
    return HealthResponse(state=status.state, version=status.version)
