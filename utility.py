"""Temperature conversion utilities."""

import math


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a finite Celsius temperature to Fahrenheit.

    Raises:
        TypeError: If ``celsius`` is not an integer or float.
        ValueError: If ``celsius`` is not finite.
    """
    if isinstance(celsius, bool) or not isinstance(celsius, (int, float)):
        raise TypeError("celsius must be a number.")

    try:
        celsius = float(celsius)
    except OverflowError as error:
        raise ValueError("celsius must be finite.") from error

    if not math.isfinite(celsius):
        raise ValueError("celsius must be finite.")

    return (celsius * 9 / 5) + 32


if __name__ == "__main__":
    print(f"20 C is {celsius_to_fahrenheit(20):.1f} F")
