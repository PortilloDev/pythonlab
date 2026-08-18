from dataclasses import dataclass
from enum import StrEnum


class HealthState(StrEnum):
    OK = "ok"
    DEGRADED = "degraded"


@dataclass(frozen=True, slots=True)
class HealthStatus:
    state: HealthState
    version: str
