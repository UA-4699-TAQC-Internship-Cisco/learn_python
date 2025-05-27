# Gap in Primes


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def gap(g, m, n):
    last_prime = None
    for num in range(m, n + 1):
        if is_prime(num):
            if last_prime is not None and num - last_prime == g:
                return [last_prime, num]
            last_prime = num
    return None

# Trailing zeros in factorial


def zeros(n):
    count = 0
    while n >= 5:
        n = n // 5
        count += n
    return count

# Perimeter of squares in a rectangle


def perimeter(n):
    a, b = 1, 1
    total = a
    for _ in range(n):
        a, b = b, a + b
        total += a
    return 4 * total

# Which x for that sum?


def solve(m):
    left = 0.0
    right = 1.0

    while right - left > 1e-13:
        mid = (left + right) / 2
        f = mid / (1 - mid) ** 2

        if f < m:
            left = mid
        else:
            right = mid

    return (left + right) / 2

# Find the smallest


def smallest(n):
    s = str(n)
    min_triplet = [n, 0, 0]

    for i in range(len(s)):
        digit = s[i]
        rest = s[:i] + s[i+1:]
        for j in range(len(s)):
            new_s = rest[:j] + digit + rest[j:]
            new_n = int(new_s)
            if new_n < min_triplet[0] or \
               (new_n == min_triplet[0] and i < min_triplet[1]) or \
               (new_n == min_triplet[0] and i == min_triplet[1] and j < min_triplet[2]):
                min_triplet = [new_n, i, j]

    return min_triplet




