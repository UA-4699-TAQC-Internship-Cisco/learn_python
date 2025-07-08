import math


# ================================================
# Gap in Primes
def gap(gap_size, start, end):
    """
    Find the first pair of primes with specified gap in given range.
    """

    def is_prime(number):
        """
        Check if a number is prime.
        """
        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        max_divisor = int(number ** 0.5) + 1
        for divisor in range(3, max_divisor, 2):
            if number % divisor == 0:
                return False
        return True

    previous_prime = None
    for current in range(start, end + 1):
        if is_prime(current):
            if (previous_prime is not None and
                    (current - previous_prime) == gap_size):
                # Verify no primes exist between them
                valid = True
                for num in range(previous_prime + 1, current):
                    if is_prime(num):
                        valid = False
                        break
                if valid:
                    return [previous_prime, current]
            previous_prime = current
    return None


# ================================================
# Trailing zeros in factorial
def zeros(number):
    """
    Calculate the number of trailing zeros in n! (n factorial).
    """
    count = 0
    while number > 0:
        number = number // 5
        count += number
    return count


# ================================================
# Perimeter of squares in a rectangle
def perimeter(number_of_terms):
    """Calculate the perimeter of a rectangle formed by Fibonacci-arranged squares.

    The perimeter is calculated as 4 times the sum of the first (n+1) Fibonacci numbers,
    which represents the arrangement of squares in a rectangle pattern.
    """
    if number_of_terms == 0:
        return 4 * 1

    previous_term, current_term = 1, 1
    sum_fibonacci = previous_term + current_term

    for _ in range(2, number_of_terms + 1):
        previous_term, current_term = current_term, previous_term + current_term
        sum_fibonacci += current_term

    return 4 * sum_fibonacci


# ================================================
# Which x for that sum?
def solve(target_sum):
    """
    Find x such that the infinite series U(n, x) converges to target_sum.

    The function solves the equation derived from the series limit:
    x/(1-x)² = target_sum for 0 < x < 1

    """
    discriminant = 4 * target_sum + 1
    sqrt_discriminant = math.sqrt(discriminant)
    solution = (2 * target_sum + 1 - sqrt_discriminant) / (2 * target_sum)
    return solution


# ================================================
# Find the smallest number
def smallest(number):
    """
    Find the smallest number by moving one digit and return the transformation details.
    """
    digits = list(str(number))
    min_number = None
    from_idx = 0
    to_idx = 0

    for i, current_digit in enumerate(digits):
        temp_digits = digits[:i] + digits[i + 1:]
        for j in range(len(temp_digits) + 1):
            new_digits = temp_digits[:j] + [current_digit] + temp_digits[j:]
            new_num = int(''.join(new_digits))
            if min_number is None or new_num < min_number:
                min_number = new_num
                from_idx = i
                to_idx = j
            elif new_num == min_number:
                if i < from_idx or (i == from_idx and j < to_idx):
                    from_idx = i
                    to_idx = j

    return [min_number, from_idx, to_idx]
