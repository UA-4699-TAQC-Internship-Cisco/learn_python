import math

def litres(time):
    return int(0.5 * time)


def get_volume_of_cuboid(a, b, h):
    return a * b * h


def converter(mpg):
    return round(mpg * 1.609344 / 4.54609188, 2)


def square_or_square_root(arr):
    return [int(math.sqrt(x)) if math.sqrt(x).is_integer() else x * x for x in arr]


def count_positives_sum_negatives(arr):
    if not arr:
        return []
    pos_count = sum(1 for x in arr if x > 0)
    neg_sum = sum(x for x in arr if x < 0)
    return [pos_count, neg_sum]


def string_to_number(s):
    return int(s)


def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def am_i_wilson(n):
    if n < 2:
        return False
    return (factorial(n - 1) + 1) % (n * n) == 0


def two_decimal_places(n):
    return round(n, 2)


def divisible_by(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]
