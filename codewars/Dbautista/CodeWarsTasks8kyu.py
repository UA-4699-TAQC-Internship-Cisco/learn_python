# Keep Hydrated!

def litres(time):
    liters= int(time * 0.5)
    return liters

# Volume of a Cuboid

def get_volume_of_cuboid(length, width, height):
    return length * width * height

# Miles per gallon to kilometers per liter

def converter(mpg):
    kpl = 1.609344/4.54609188*mpg
    return round(kpl, 2)

# To square(root) or not to square(root)

def square_or_square_root(arr):
    result = []
    for i in arr: 
        if (i ** 0.5).is_integer():
            result.append(i ** 0.5) 
        else: 
            result.append(i **2) 
    return result

# Count of positives / sum of negatives

def count_positives_sum_negatives(arr):
    if not arr:
        return []

    result = []
    positive = 0
    negative = 0

    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += i

    result.append(positive)
    result.append(negative)
    return result

# Convert a String to a Number!

def string_to_number(s):
   return int(s)

# Wilson primes

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def am_i_wilson(result):
    if result < 2:
        return False

    for i in range(2, int(result ** 0.5) + 1):
        if result % i == 0:
            return False

    return ((factorial(result - 1) + 1) % (result * result)) == 0

# Коротка версія
# def am_i_wilson(p):
#     return p in (5, 13, 563)

# Formatting decimal places #0

def two_decimal_places(n):
    
    return round(n, 2)

    raise NotImplementedError("TODO: two_decimal_places")

# Find numbers which are divisible by given number

def divisible_by(numbers, divisor):
    result = []
    for i in numbers:
        if i == 0:
            result.append(i)   
        elif i%divisor == 0:
            result.append(i)
    return result
            