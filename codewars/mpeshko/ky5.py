def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gap(g, m, n):
    prev_prime = None
    for i in range(m, n + 1):
        if is_prime(i):
            if prev_prime and i - prev_prime == g:
                return [prev_prime, i]
            prev_prime = i
    return None

def zeros(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count

def perimeter(n):
    fib = [1, 1]
    while len(fib) <= n + 1:
        fib.append(fib[-1] + fib[-2])
    return sum(fib[:n + 1]) * 4

def solve(m):
    left = 0.0
    right = 1.0
    eps = 1e-12
    while right - left > eps:
        mid = (left + right) / 2
        series_sum = mid / (1 - mid)**2
        if series_sum < m:
            left = mid
        else:
            right = mid
    return (left + right) / 2

def smallest(n):
    s = str(n)
    best = (n, 0, 0)
    for i in range(len(s)):
        removed = s[:i] + s[i+1:]
        for j in range(len(removed)+1):
            candidate = int(removed[:j] + s[i] + removed[j:])
            if (candidate < best[0]) or (candidate == best[0] and (i < best[1] or (i == best[1] and j < best[2]))):
                best = (candidate, i, j)
    return list(best)
