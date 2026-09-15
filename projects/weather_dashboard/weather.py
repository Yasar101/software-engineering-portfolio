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


def main() -> None:
    """Fetch current weather through the Open-Meteo adapter."""
    import argparse
    from urllib.error import URLError

    parser = argparse.ArgumentParser(description="Fetch current conditions from Open-Meteo.")
    parser.add_argument("latitude", type=float)
    parser.add_argument("longitude", type=float)
    parser.add_argument("--timeout", type=float, default=5, help="network timeout in seconds")
    args = parser.parse_args()
    if not -90 <= args.latitude <= 90 or not -180 <= args.longitude <= 180 or args.timeout <= 0:
        parser.error("use valid latitude/longitude values and a positive timeout")
    try:
        snapshot = fetch_weather(args.latitude, args.longitude, args.timeout)
    except (URLError, TimeoutError, ValueError) as exc:
        parser.error(f"weather provider unavailable or returned invalid data: {exc}")
    print(snapshot.summary)
    print(f"Observed at: {snapshot.observed_at}")
    print("Provider: Open-Meteo. Conditions are live at request time, not stored history.")


if __name__ == "__main__":
    main()
