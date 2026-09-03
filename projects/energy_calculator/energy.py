"""Energy, cost, and carbon estimation."""

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP


@dataclass(frozen=True)
class EnergyEstimate:
    kwh: Decimal
    cost: Decimal
    carbon_kg: Decimal


def estimate_energy(watts: Decimal, hours_per_day: Decimal, days: int, tariff_per_kwh: Decimal, carbon_kg_per_kwh: Decimal = Decimal("0.207")) -> EnergyEstimate:
    if watts < 0 or hours_per_day < 0 or days < 0 or tariff_per_kwh < 0 or carbon_kg_per_kwh < 0:
        raise ValueError("inputs cannot be negative")
    if hours_per_day > 24:
        raise ValueError("hours per day cannot exceed 24")
    kwh = watts * hours_per_day * days / Decimal("1000")
    money = Decimal("0.01")
    carbon = Decimal("0.001")
    return EnergyEstimate(kwh.quantize(carbon, rounding=ROUND_HALF_UP), (kwh * tariff_per_kwh).quantize(money, rounding=ROUND_HALF_UP), (kwh * carbon_kg_per_kwh).quantize(carbon, rounding=ROUND_HALF_UP))
