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



# Find the smallest




