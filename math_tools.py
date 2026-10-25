def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(number):
    """Return True if number is a prime number, otherwise False."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True


if __name__ == "__main__":
    print("Example usage:")
    print(f"factorial(5) = {factorial(5)}")
    print(f"is_prime(17) = {is_prime(17)}")
    print(f"is_prime(18) = {is_prime(18)}")
