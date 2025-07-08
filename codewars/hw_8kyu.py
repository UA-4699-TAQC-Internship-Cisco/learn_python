# Keep Hydrated!
def litres(time):
    """
    This module calculates the amount of water Nathan should drink while cycling,
    based on the time spent cycling. Nathan drinks 0.5 litres of water per hour.
    """
    return int(time * 0.5)


# ================================================
# Volume of a Cuboid
def get_volume_of_cuboid(length, width, height):
    """
    This module provides a function to calculate the volume of a rectangular cuboid
    given its length, width, and height measurements.
    """
    return length * width * height


# ================================================
# Miles per gallon to kilometers per liter
LITRES_PER_GALLON = 4.54609188
KILOMETERS_PER_MILE = 1.609344


def converter(mpg):
    """
    This module converts miles per imperial gallon (mpg)
    to kilometers per liter (kpl).
    """
    kpl = (mpg * KILOMETERS_PER_MILE) / LITRES_PER_GALLON
    return round(kpl, 2)


# ================================================
# To square(root) or not to square(root)
def square_or_square_root(arr):
    """
    This module processes an array of numbers by taking square roots of perfect
    squares and squaring other numbers.
    """
    processed = []
    for number in arr:
        sqrt_num = number ** 0.5
        if sqrt_num.is_integer():
            processed.append(int(sqrt_num))
        else:
            processed.append(number * number)
    return processed


# ================================================
# Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    """
    This module processes an array of integers to count positive numbers
    and sum negative numbers.
    """
    if not arr:
        return []

    positives = sum(1 for num in arr if num > 0)
    negatives = sum(num for num in arr if num < 0)
    return [positives, negatives]


# ================================================
# Convert a String to a Number!
def string_to_number(string_input):
    """
    This module convert string to  integer.
    """
    return int(string_input)


# ================================================
# Wilson primes
def am_i_wilson(n):
    nums = [5, 13, 563]
    return n in nums


# ================================================
# Formatting decimal places #0
def two_decimal_places(number):
    """
    This module provides functionality to format numbers
    with two decimal places rounding.
    """
    return round(number, 2)


# ================================================
# Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    """
    Find numbers divisible by a given divisor.
    """
    return [num for num in numbers if num % divisor == 0]

