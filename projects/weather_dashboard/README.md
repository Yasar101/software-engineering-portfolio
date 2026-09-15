# Weather Dashboard Core

**TESTED CORE** · [Portfolio](../../README.md) · [Architecture](../../docs/ARCHITECTURE.md) · [Live demo](https://yasar101.github.io/software-engineering-portfolio/demos/weather-dashboard.html)

An Open-Meteo response parser, display model and HTTP fetch function; no dashboard UI.

## Purpose and engineering skills

Separate external transport from parsing so useful behavior can be tested offline.

## Structure

weather.py defines WeatherSnapshot, parse_open_meteo and fetch_weather. [Source](weather.py).

## Run

From the repository root with Python 3.11+, run this offline example using `python3` (no dependencies or credentials):

```python
from projects.weather_dashboard import parse_open_meteo
weather = parse_open_meteo({"current": {"temperature_2m": 18.5, "wind_speed_10m": 9, "time": "2026-09-08T12:00"}})
print(weather.summary)
```

## Test

```sh
python3 -m unittest tests.test_foundations.WeatherTests -v
python3 -m unittest discover -s tests -v
```

The full suite also includes release regression tests and executes these README examples.

## Complete and remaining

**Complete:** Required-field parsing, numeric conversion and display formatting. The HTTP adapter exists; the example uses a local fixture.

**Remaining / limitations:** Live API behavior is unverified. No UI, retries, caching or location validation; network errors propagate.

## Learning takeaway

A presentation model can be validated without making a flaky live API call.

## Command-line demonstration
Fetch current conditions when network access is available:

```bash
python3 -m projects.weather_dashboard 51.5072 -0.1276
```

The CLI validates coordinates and provider failures. For an offline, deterministic
fixture demonstration, run `python3 demo.py weather` from the repository root.
