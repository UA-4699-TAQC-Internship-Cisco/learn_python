"""Auto-formatted with proper docstrings and variable renaming."""
import math

def litres(time):
    """Calculate how many litres Nathan will drink, assuming 0.5 litres per hour.

    Args:
        time (float): Time in hours.

    Returns:
        int: Litres consumed, rounded down.
    """
    return int(0.5 * time)

def get_volume_of_cuboid(length_a, length_b, height):
    """Return volume of a cuboid given length, width and height.

    Args:
        length_a (float): Length.
        length_b (float): Width.
        height (float): Height.

    Returns:
        float: Volume.
    """
    return length_a * length_b * height

def converter(mpg):
    """Convert miles per gallon to kilometers per liter.

    Args:
        mpg (float): Miles per gallon.

    Returns:
        float: Kilometers per liter rounded to 2 decimal places.
    """
    return round(mpg * 1.609344 / 4.54609188, 2)

def square_or_square_root(arr):
    """Return list where square roots are replaced with int if whole, else square the number.

    Args:
        arr (list of int): Input list.

    Returns:
        list of int: Transformed list.
    """
    return [int(math.sqrt(x)) if math.sqrt(x).is_integer() else x * x for x in arr]

def count_positives_sum_negatives(arr):
    """Return list with count of positives and sum of negatives.

    Args:
        arr (list of int): Input list.

    Returns:
        list: [positive count, sum of negatives]
    """
    if not arr:
        return []
    pos_count = sum(1 for x in arr if x > 0)
    neg_sum = sum(x for x in arr if x < 0)
    return [pos_count, neg_sum]

def string_to_number(string_input):
    """Convert a string to an integer.

    Args:
        string_input (str): Input string.

    Returns:
        int: Converted integer.
    """
    return int(string_input)

def factorial(number):
    """Calculate factorial of a number.

    Args:
        number (int): Input integer.

    Returns:
        int: Factorial result.
    """
    res = 1
    for i in range(2, number + 1):
        res *= i
    return res

def am_i_wilson(number):
    """Check if a number is a Wilson prime.

    Args:
        number (int): Input number.

    Returns:
        bool: True if Wilson prime, False otherwise.
    """
    if number < 2:
        return False
    return (factorial(number - 1) + 1) % (number * number) == 0

def two_decimal_places(number):
    """Round a number to two decimal places.

    Args:
        number (float): Input number.

    Returns:
        float: Rounded value.
    """
    return round(number, 2)

def divisible_by(numbers, divisor):
    """Return a list of numbers divisible by the given divisor.

    Args:
        numbers (list of int): List of numbers.
        divisor (int): The divisor.

    Returns:
        list of int: Numbers divisible by divisor.
    """
    return [x for x in numbers if x % divisor == 0]
