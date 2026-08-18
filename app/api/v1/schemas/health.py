from pydantic import BaseModel

from app.domain.health.entities import HealthState


class HealthResponse(BaseModel):
    state: HealthState
    version: str
