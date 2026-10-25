# Math Tools

`math_tools.py` provides functions for calculating factorials and checking
whether a number is prime.

## Example

Import the functions into your Python code:

```python
from math_tools import factorial, is_prime

print(factorial(5))  # 120
print(is_prime(17))  # True
print(is_prime(18))  # False
```

You can also run the module directly to see example output:

```bash
python math_tools.py
```

## Celsius to Fahrenheit

Use `utility.py` to convert a Celsius temperature:

```python
from utility import celsius_to_fahrenheit

print(celsius_to_fahrenheit(20))  # 68.0
```

The function rejects non-numeric and non-finite values. Run the script directly
for a short example:

```bash
python utility.py
```

## Tests

Run the unit tests with:

```bash
python -m unittest -v
```

## Normalize contacts CSV

The `normalize_contacts.py` script reads a CSV with `Name` and `Email` columns,
collapses whitespace and applies Unicode compatibility normalization to text
values in those columns, and lowercases email addresses. Other columns are
preserved.

```bash
python normalize_contacts.py contacts.csv normalized_contacts.csv
```
