#1
def litres(time):
    return int(time * 0.5)

#2
def get_volume_of_cuboid(length, width, height):
    return length * width * height

#3
def converter(mpg):
    miles_to_km = 1.609344
    gallons_to_litres = 4.54609188
    kpl = (mpg * miles_to_km) / gallons_to_litres
    return round (kpl, 2)
#4
def square_or_square_root(arr):
    result = []
    for num in arr:
        root = num ** 0.5
        if root.is_integer():
            result.append(int(root))
        else:
            result.append(num ** 2)
    return result

#5
def count_positives_sum_negatives(arr):
    if not arr:
        return []

    count_positive = sum(1 for x in arr if x > 0)
    sum_negative = sum(x for x in arr if x < 0)

    return [count_positive, sum_negative]

#6
def string_to_number(s):
    return int(s)

#7
def am_i_wilson(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    factorial = 1
    for i in range(1, n):
        factorial *= i

    return (factorial + 1) % (n * n) == 0

#8
def two_decimal_places(n):
    return round(n, 2)
#9
def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]