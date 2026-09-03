"""Weather data adapter and presentation model."""

from dataclasses import dataclass
import json
from urllib.parse import urlencode
from urllib.request import urlopen


@dataclass(frozen=True)
class WeatherSnapshot:
    temperature_c: float
    wind_speed_kph: float
    observed_at: str

    @property
    def summary(self) -> str:
        return f"{self.temperature_c:.1f}°C, wind {self.wind_speed_kph:.1f} km/h"


def parse_open_meteo(payload: dict[str, object]) -> WeatherSnapshot:
    try:
        current = payload["current"]
        if not isinstance(current, dict):
            raise TypeError
        return WeatherSnapshot(float(current["temperature_2m"]), float(current["wind_speed_10m"]), str(current["time"]))
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("invalid weather response") from exc


def fetch_weather(latitude: float, longitude: float, timeout: float = 5) -> WeatherSnapshot:
    query = urlencode({"latitude": latitude, "longitude": longitude, "current": "temperature_2m,wind_speed_10m"})
    with urlopen(f"https://api.open-meteo.com/v1/forecast?{query}", timeout=timeout) as response:  # noqa: S310
        return parse_open_meteo(json.load(response))
