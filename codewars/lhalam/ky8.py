# -*- coding: utf-8 -*-
import math

def litres(time):
    if time > 0:
        return int(time*0.5)
    else:
        return u"Are you Christopher Nolan?"


def volume_of_a_rectangular_cuboid(length, width, height):
    if length>0 and width>0 and height>0:
        return length*width*height
    else:
        return u"It is not a rectangular cuboid. Please check your data."


def convert_mpg_to_kpl(mpg):
    # 1 імперський галон = 4, 54609188 літра
    # 1 миля = 1, 609344 кілометра
    kilometres_per_litres = 1.609344/4.54609188
    result = mpg*kilometres_per_litres
    return round(result, 2)


def square_root_or_not(array):
    result = []
    for a in array:
        if int(a**0.5) == (a**0.5):
            result.append(int(a**0.5))
        else:
            result.append(int(a**2))
    return result


def count_positives_sum_negatives(array):
    if len(array) == 0:
        return []
    else:
        positives_count = 0
        negatives_sum = 0
        for a in array:
            if a == 0:
                pass
            elif a > 0:
                positives_count += 1
            elif a < 0:
                negatives_sum += a
        if positives_count == 0 and negatives_sum == 0:
            return []
        else:
            return [positives_count, negatives_sum]


def  convert_string_to_number(string):
    return int(string)


def is_wilson_prime(p):
    if p < 2:
        return False
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False

    numerator = math.factorial(p - 1) + 1
    denominator = p * p

    return numerator % denominator == 0


def formatting_decimal_places (num):
    return round(num, 2)


def  divisible_by_number(arr, num):
    result = []
    for a in arr:
        if a % num == 0:
            result.append(a)
    return result

