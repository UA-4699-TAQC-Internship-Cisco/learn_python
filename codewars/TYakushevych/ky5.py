# -*- coding: utf-8 -*-

def is_prime(number): #helper function for gap
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True



def gap(g, m, n):#Gap in Primes
    """Find a pair of two prime numbers which difference is equal to g."""
    previous = m

    for i in range(m, n + 1):
        current = i
        if is_prime(current):
            if current - previous == g:
                return [previous, current]

            previous = current

    return None


def zeros(number): #Number of trailing zeros of N!
    """Calculate the count of trailing zeros of N!"""
    count = 0
    i = 5
    while number // i > 0:
        count += number // i
        i *= 5
    return count



def perimeter(number): #Perimeter of squares in a rectangle
    """Return the total perimeter of Fibonacci squares."""
    previous, current = 1, 1
    result = [previous]

    for _ in range(number):
        result.append(current)
        previous, current = current, previous + current

    return sum(result) * 4



def solve(m): #Which x for that sum?
    """Solve equation using binary search"""
    left = 0.0
    right = 1.0
    exponent = 1e-12

    while right - left > exponent:
        mid = (left + right) / 2.0
        series_sum = mid / (1 - mid)**2

        if series_sum < m:
            left = mid
        else:
            right = mid

    return (left + right) / 2.0


def smallest(number): #Find the smallest
    """Find the smallest number from the different digits of given number."""
    str_num = str(number)
    best_num = number
    best_i = 0
    best_j = 0

    for i in range(len(str_num)):
        digit = str_num[i]

        rest = str_num[:i] + str_num[i + 1:]

        for j in range(len(rest) + 1):

            new_s = rest[:j] + digit + rest[j:]
            new_num = int(new_s)

            if (new_num < best_num or
                    (new_num == best_num and (i < best_i or (i == best_i and j < best_j)))):
                best_num = new_num
                best_i = i
                best_j = j

    return [best_num, best_i, best_j]