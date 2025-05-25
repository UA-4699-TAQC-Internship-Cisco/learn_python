# -*- coding: utf-8 -*-
import math

def litres(time): #Keep Hydrated!
     return math.floor(0.5 * time)


def get_volume_of_cuboid(a, b, h): #Volume of a Cuboid
    return a * b * h


def converter(mpg): #Miles per gallon to kilometers per liter
    return round(mpg * 1.609344/4.54609188, 2)


def square_or_square_root(arr): #To square(root) or not to square(root)
    return [math.sqrt(elem) if math.sqrt(elem) == int(math.sqrt(elem)) else elem ** 2 for elem in arr]


def count_positives_sum_negatives(arr): #Count of positives / sum of negatives
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



def string_to_number(s):#Convert a String to a Number!
    # your code here
    try:
        return int(s)
    except ValueError:
        print "Can't convert string to int"


def factorial(n): #helper for am I wilson
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def am_i_wilson(n): #Wilson primes
    if n <2:
        return False
    return ((factorial(n - 1) + 1) % (n * n)) == 0


def two_decimal_places(n): #Formatting decimal places
    return round(n, 2)




def divisible_by(numbers, divisor): #Find numbers which are divisible by given number
    return [elem  for elem in numbers if elem % divisor == 0]













