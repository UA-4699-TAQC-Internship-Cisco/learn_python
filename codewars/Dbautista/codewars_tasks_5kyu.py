"""This module contains multiple utility functions for prime gaps, factorial zeros,
perimeter of Fibonacci squares, binary search, and digit rearrangement tasks."""


def is_prime(number):
    """Check if a number is a prime."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def gap(gap_size, start, end):
    """Find the first pair of two prime numbers spaced with a gap of `gap_size` between them."""
    previous = None
    for number in range(start, end + 1):
        if is_prime(number):
            if previous is not None and number - previous == gap_size:
                return [previous, number]
            previous = number
    return None


def trailing_zeros_in_factorial(number):
    """Return the number of trailing zeros in number! (factorial)."""
    count = 0
    factor = 5
    while number // factor > 0:
        count += number // factor
        factor *= 5
    return count


def perimeter_of_fibonacci_squares(length):
    """Return the total perimeter of (length + 1) Fibonacci squares."""
    first, second = 0, 1
    total = 0
    for _ in range(length + 1):
        total += second
        first, second = second, first + second
    return 4 * total


def solve_for_sum(target_sum):
    """Solve equation x / (1 - x)^2 = target_sum for x using binary search."""
    def function(value):
        """The function to solve."""
        return value / (1 - value) ** 2

    left = 0.0
    right = 1.0
    while right - left > 1e-14:
        mid = (left + right) / 2
        if function(mid) < target_sum:
            left = mid
        else:
            right = mid
    return (left + right) / 2


def find_smallest_by_moving_digit(number):
    """Find the smallest number by moving one digit in number and return the number and positions."""
    digits_str = str(number)
    minimum = number
    from_index = to_index = 0

    for i in range(len(digits_str)):
        for j in range(len(digits_str)):
            if i == j:
                continue
            digits = list(digits_str)
            digit = digits.pop(i)
            digits.insert(j, digit)
            new_number = int(''.join(digits))
            if new_number < minimum:
                minimum = new_number
                from_index = i
                to_index = j
            elif new_number == minimum:
                if i < from_index or (i == from_index and j < to_index):
                    from_index = i
                    to_index = j

    return [minimum, from_index, to_index]
