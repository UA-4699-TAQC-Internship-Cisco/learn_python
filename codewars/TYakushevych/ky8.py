import math

def litres(time): #Keep Hydrated!
    """Return number of litres that will drink by the  time"""
    return math.floor(0.5 * time)



def get_volume_of_cuboid(a, b, h): #Volume of a Cuboid
    """Return volume of a cuboid"""
    return a * b * h


def converter(mpg): #Miles per gallon to kilometers per liter
    """Convert miles per gallon to kilometers per liter"""
    return round(mpg * 1.609344/4.54609188, 2)


def square_or_square_root(arr): #To square(root) or not to square(root)
    """Return square root  of number or number ** 2   of a list"""
    return [
        math.sqrt(elem) if math.sqrt(elem) == int(math.sqrt(elem)) else elem ** 2 for elem in arr
    ]


def count_positives_sum_negatives(arr): #Count of positives / sum of negatives
    """Calculate the count of positive and sum of negative numbers"""
    result = []
    n_suma = 0
    pos_counter = 0

    if not arr:
        return []

    for elem in arr:
        if elem > 0:
            pos_counter += 1
        elif elem < 0:
            n_suma += elem

    result.append(pos_counter)
    result.append(n_suma)
    return result



def string_to_number(string):#Convert a String to a Number!
    """Convert string to number"""
    try:
        return int(string)
    except ValueError:
        print "Can't convert string to int"


def factorial(number): #helper for am I wilson
    """Return the factorial of a number"""
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result

def am_i_wilson(number): #Wilson primes
    """Check if the number is a Wilson number"""
    if number < 2:
        return False
    return ((factorial(number - 1) + 1) % (number * number)) == 0


def two_decimal_places(number): #Formatting decimal places
    """Formatting decimal number to two decimal places"""
    return round(number, 2)




def divisible_by(numbers, divisor): #Find numbers which are divisible by given number
    """Find numbers which are divisible by given number"""

    return [elem  for elem in numbers if elem % divisor == 0]


