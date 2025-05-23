# Keep Hydrated!

import math


def litres(time):
    return math.floor(time * 0.5)


# Volume of a cuboid


def get_volume_of_cuboid(length, width, height):
    return length * width * height


# Miles per gallon to kilometers per liter


def converter(mpg):
    return round(mpg * 1.609344 / 4.54609188, 2)


# To square root or no to square


def square_or_square_root(arr):
    result = []
    for n in arr:
        root = math.sqrt(n)
        if root.is_integer():
            result.append(int(root))
        else:
            result.append(n ** 2)
    return result


# Count of positives / sum of negatives


def count_positives_sum_negatives(arr):
    if not arr:
        return []
    else:
        a = 0
        b = 0
        for i in arr:
            if i > 0:
                a += 1
            elif i < 0:
                b += i

        return [a, b]


# Convert a String to a Number


def string_to_number(s):
    return int(s)


# Willson primes


def am_i_wilson(n):
    return n in {5, 13, 563}


# Formatting decimal places


def two_decimal_places(n):
    return round(n, 2)

# Find numbers which are divisible by given number


def divisible_by(numbers, divisor):
    result = []
    for i in numbers:
        if i % divisor == 0:
            result.append(i)
    return result
