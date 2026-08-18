from app.core.config import Settings, get_settings
from app.domain.health.entities import HealthState, HealthStatus


class GetHealthStatus:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def execute(self) -> HealthStatus:
        return HealthStatus(state=HealthState.OK, version=self._settings.version)


def get_health_status_use_case() -> GetHealthStatus:
    return GetHealthStatus(settings=get_settings())
