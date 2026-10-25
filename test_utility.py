import unittest

from utility import celsius_to_fahrenheit


class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_converts_integer_temperature(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_converts_fractional_temperature(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(37.5), 99.5)

    def test_rejects_non_numeric_input(self):
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit("20")

    def test_rejects_non_finite_input(self):
        for temperature in (float("nan"), float("inf"), float("-inf")):
            with self.subTest(temperature=temperature):
                with self.assertRaises(ValueError):
                    celsius_to_fahrenheit(temperature)

    def test_rejects_boolean_input(self):
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit(True)


if __name__ == "__main__":
    unittest.main()
