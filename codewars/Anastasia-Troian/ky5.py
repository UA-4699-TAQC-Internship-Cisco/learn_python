#18
def is_prime(num):
    #Helper function to check if a number is prime.
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def gap(g, m, n):
    #Find the first pair of primes with a gap of g between m and n.
    previous_prime = None

    for current in range(m, n + 1):
        if is_prime(current):
            if previous_prime and current - previous_prime == g:
                return [previous_prime, current]
            previous_prime = current

    return None

#19
def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

#20
def perimeter(n):
    a, b = 1, 1
    fib_sum = a

    for _ in range(n):
        a, b = b, a + b
        fib_sum += a

    return 4 * fib_sum

#21
def solve(m):
    left, right = 0.0, 1.0
    for _ in range(100):
        mid = (left + right) / 2.0
        val = mid / (1 - mid) ** 2
        if abs(val - m) < 1e-13:
            return mid
        if val < m:
            left = mid
        else:
            right = mid
    return (left + right) / 2.0

#22
def smallest(n):
    s = list(str(n))
    length = len(s)
    min_num = n
    res = [n, 0, 0]
    for i in range(length):
        digit = s[i]
        temp = s[:i] + s[i+1:]
        for j in range(length):
            new_s = temp[:j] + [digit] + temp[j:]
            new_num = int("".join(new_s))
            if new_num < min_num:
                min_num = new_num
                res = [new_num, i, j]
            elif new_num == min_num:
                if i < res[1] or (i == res[1] and j < res[2]):
                    res = [new_num, i, j]
    return res