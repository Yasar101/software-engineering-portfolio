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


def main() -> None:
    """Calculate a transparent local electricity estimate."""
    import argparse
    from decimal import InvalidOperation

    parser = argparse.ArgumentParser(description="Estimate electricity use, cost, and carbon from local inputs.")
    parser.add_argument("--watts", required=True, help="appliance power in watts")
    parser.add_argument("--hours", required=True, help="hours used per day")
    parser.add_argument("--days", required=True, type=int, help="billing-period days")
    parser.add_argument("--tariff", required=True, help="price per kWh in GBP")
    parser.add_argument("--carbon", default="0.207", help="kg CO2e per kWh (default: 0.207)")
    args = parser.parse_args()
    try:
        result = estimate_energy(Decimal(args.watts), Decimal(args.hours), args.days, Decimal(args.tariff), Decimal(args.carbon))
    except (ValueError, InvalidOperation) as exc:
        parser.error(str(exc))
    print(f"Consumption: {result.kwh} kWh")
    print(f"Estimated electricity cost: £{result.cost}")
    print(f"Estimated carbon: {result.carbon_kg} kg CO2e")
    print("Estimate only; no supplier data or tariff integration is used.")


if __name__ == "__main__":
    main()
