# Gap in Primes


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def gap(gap_size, start, end):
    last_prime = None
    for num in range(start, end + 1):
        if is_prime(num):
            if last_prime is not None and num - last_prime == gap_size:
                return [last_prime, num]
            last_prime = num
    return None

# Trailing zeros in factorial


def zeros(number):
    count = 0
    while number >= 5:
        number = number // 5
        count += number
    return count

# Perimeter of squares in a rectangle


def perimeter(fib_terms_count):
    first, second = 1, 1
    total_sum = first
    for _ in range(fib_terms_count):
        first, second = second, first + second
        total_sum += first
    return 4 * total_sum

# Which x for that sum?


def solve(target_value):
    left_bound = 0.0
    right_bound = 1.0

    while right_bound - left_bound > 1e-13:
        midpoint = (left_bound + right_bound) / 2
        f_value = midpoint / (1 - midpoint) ** 2

        if f_value < target_value:
            left_bound = midpoint
        else:
            right_bound = midpoint

    return (left_bound + right_bound) / 2


# Find the smallest


def smallest(number):
    number_str = str(number)
    min_triplet = [number, 0, 0]

    for i, digit in enumerate(number_str):
        rest = number_str[:i] + number_str[i+1:]
        for j in range(len(number_str)):
            new_s = rest[:j] + digit + rest[j:]
            new_n = int(new_s)
            is_smaller_number = new_n < min_triplet[0]
            is_same_number_but_lower_i = new_n == min_triplet[0] and i < min_triplet[1]
            is_same_number_i_but_lower_j = (new_n == min_triplet[0]
                                            and i == min_triplet[1] and j < min_triplet[2])
            if is_smaller_number or is_same_number_but_lower_i or is_same_number_i_but_lower_j:
                min_triplet = [new_n, i, j]

    return min_triplet
