# -*- coding: utf-8 -*-


def gap(g, m, n):
    def is_prime(x):
        if x < 2:
            return False
        for i in xrange(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    prev = None
    for i in xrange(m, n + 1):
        if is_prime(i):
            if prev and i - prev == g:
                return [prev, i]
            prev = i
    return None


def trailing_zeros(n):
    if n < 0:
        return -1

    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


def perimeter_fibonacci(n):
    a, b = 0, 1
    total = 0
    for i in xrange(n + 1):
        total += b
        a, b = b, a + b
    return 4 * total


def x_for_sum(m):
    def f(x):
        return x / ((1 - x) ** 2)

    low = 0.0
    high = 1.0
    while high - low > 1e-13:
        mid = (low + high) / 2
        if f(mid) < m:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def smallest(n):
    s = str(n)
    min_number = int(s)
    from_i, to_j = 0, 0

    for i in xrange(len(s)):
        for j in xrange(len(s)):
            if i == j:
                continue
            temp = list(s)
            digit = temp.pop(i)
            temp.insert(j, digit)
            candidate = int("".join(temp))
            if candidate < min_number:
                min_number = candidate
                from_i, to_j = i, j
    return [min_number, from_i, to_j]

