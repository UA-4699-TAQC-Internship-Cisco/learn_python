"""Auto-formatted with proper docstrings and variable renaming."""


def is_prime(number):
    """Check if a number is a prime number."""
    if number < 2:
        return False
    for input_value in range(2, int(number ** 0.5) + 1):
        if number % input_value == 0:
            return False
    return True


def gap(gap_value, value, number):
    """Find the first pair of prime numbers within a given range with a specific gap."""
    prev_prime = None
    for input_value in range(value, number + 1):
        if is_prime(input_value):
            if prev_prime and input_value - prev_prime == gap_value:
                return [prev_prime, input_value]
            prev_prime = input_value
    return None


def zeros(number):
    """Calculate the number of trailing zeros in a factorial of a given number."""
    count = 0
    input_value = 5
    while number // input_value > 0:
        count += number // input_value
        input_value *= 5
    return count


def perimeter(number):
    """Return the perimeter of squares in the Fibonacci sequence up to a given index."""
    fib = [1, 1]
    while len(fib) <= number + 1:
        fib.append(fib[-1] + fib[-2])
    return sum(fib[:number + 1]) * 4


def solve(value):
    """Find the number such that the infinite series equals a given value using binary search."""

    left = 0.0
    right = 1.0
    eps = 1e-12
    while right - left > eps:
        mid = (left + right) / 2
        series_sum = mid / (1 - mid) ** 2
        if series_sum < value:
            left = mid
        else:
            right = mid
    return (left + right) / 2


def smallest(number):
    """Return the smallest number by moving one digit to another position."""
    string_input = str(number)
    best = (number, 0, 0)
    for i, digit in enumerate(string_input):
        removed = string_input[:i] + string_input[i + 1:]
        for j in range(len(removed) + 1):
            candidate = int(removed[:j] + digit + removed[j:])
            if (
                    candidate < best[0]
                    or (candidate == best[0] and (i < best[1] or (i == best[1] and j < best[2])))
            ):
                best = (candidate, i, j)
    return list(best)
