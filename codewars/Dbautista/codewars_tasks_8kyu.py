# Keep Hydrated!
def litres(time):
    """Calculate how many liters of water Nathan will drink given time in hours."""
    return int(time * 0.5)


# Volume of a Cuboid
def get_volume_of_cuboid(length, width, height):
    """Calculate the volume of a cuboid."""
    return length * width * height


# Miles per gallon to kilometers per liter
def converter(mpg):
    """Convert miles per gallon to kilometers per liter, rounded to 2 decimals."""
    kpl = 1.609344 / 4.54609188 * mpg
    return round(kpl, 2)


# To square(root) or not to square(root)
def square_or_square_root(arr):
    """For each number in the list, square it if not a perfect square,
    else take the square root."""
    result = []
    for i in arr:
        root = i ** 0.5
        if root.is_integer():
            result.append(root)
        else:
            result.append(i ** 2)
    return result


# Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    """Return a list with count of positive numbers and sum of negative numbers."""
    if not arr:
        return []

    positive_count = 0
    negative_sum = 0

    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_sum += num

    return [positive_count, negative_sum]


# Convert a String to a Number!
def string_to_number(s):
    """Convert string to integer."""
    return int(s)


# Wilson primes
def factorial(n):
    """Calculate factorial of n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def am_i_wilson(p):
    """Check if p is a Wilson prime."""
    if p < 2:
        return False

    # Check if prime
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False

    return (factorial(p - 1) + 1) % (p * p) == 0


# Formatting decimal places #0
def two_decimal_places(n):
    """Round number to two decimal places."""
    return round(n, 2)


# Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    """Return numbers divisible by divisor."""
    return [i for i in numbers if i == 0 or i % divisor == 0]
