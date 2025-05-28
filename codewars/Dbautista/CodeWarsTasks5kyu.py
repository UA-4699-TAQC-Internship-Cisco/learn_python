# Gap in Primes

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def gap(g, m, n):
    prev = None
    for num in range(m, n + 1):
        if is_prime(num):
            if prev is not None and num - prev == g:
                return [prev, num]
            prev = num
    return None


# Number of trailing zeros of N!

def zeros(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count

# Perimeter of squares in a rectangle

def perimeter(n):
    a, b = 0, 1
    total = 0
    for _ in range(n + 1):
        total += b
        a, b = b, a + b
    return 4 * total

# Which x for that sum?

def solve(m):
    def f(x):
        return x / (1 - x)**2

    left, right = 0.0, 1.0
    while right - left > 1e-14:
        mid = (left + right) / 2
        if f(mid) < m:
            left = mid
        else:
            right = mid
    return (left + right) / 2


# Find the smallest

def smallest(n):
    s = str(n)
    min_number = n
    from_idx = to_idx = 0

    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                continue
            digits = list(s)
            digit = digits.pop(i)
            digits.insert(j, digit)
            new_number = int(''.join(digits))
            if new_number < min_number:
                min_number = new_number
                from_idx = i
                to_idx = j
            elif new_number == min_number:
                
                if i < from_idx or (i == from_idx and j < to_idx):
                    from_idx = i
                    to_idx = j

    return [min_number, from_idx, to_idx]

