# -*- coding: utf-8 -*-

def is_prime(n): #helper function for gap
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def gap(g, m, n):#Gap in Primes
    prev = m

    for i in range(m, n + 1):
        current = i
        if is_prime(current):
            if current - prev == g:
                return [prev, current]

            prev = current



def zeros(n): #Number of trailing zeros of N!
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count




def perimeter(n): #Perimeter of squares in a rectangle
    # your code
    pr, cur = 1, 1
    result = [pr]

    for _ in range(n):
        result.append(cur)
        pr, cur = cur, pr + cur

    return sum(result) * 4



def solve(m): #Which x for that sum?
    # your code
    left = 0.0
    right = 1.0
    e = 1e-12

    while right - left > e:
        mid = (left + right) / 2.0
        series_sum = mid / (1 - mid)**2

        if series_sum < m:
            left = mid
        else:
            right = mid

    return (left + right) / 2.0


def smallest(n): #Find the smallest
    s = str(n)
    best_num = n
    best_i = 0
    best_j = 0

    for i in range(len(s)):
        digit = s[i]

        rest = s[:i] + s[i + 1:]

        for j in range(len(rest) + 1):

            new_s = rest[:j] + digit + rest[j:]
            new_num = int(new_s)

            if new_num < best_num or (new_num == best_num and (i < best_i or (i == best_i and j < best_j))):
                best_num = new_num
                best_i = i
                best_j = j

    return [best_num, best_i, best_j]

