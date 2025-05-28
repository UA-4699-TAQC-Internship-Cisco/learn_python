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
    for i in arr:
        root = math.sqrt(i)
        if root.is_integer():
            result.append(int(root))
        else:
            result.append(i ** 2)
    return result


# Count of positives / sum of negatives


def count_positives_sum_negatives(arr):
    positive_count = 0
    negative_sum = 0
    result = []

    if arr:
        for num in arr:
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_sum += num
        result = [positive_count, negative_sum]

    return result


# Convert a String to a Number


def string_to_number(my_string):
    return int(my_string)


# Willson primes


def am_i_wilson(number):
    return number in {5, 13, 563}


# Formatting decimal places


def two_decimal_places(number):
    return round(number, 2)

# Find numbers which are divisible by given number


def divisible_by(numbers, divisor):
    result = []
    for i in numbers:
        if i % divisor == 0:
            result.append(i)
    return result
