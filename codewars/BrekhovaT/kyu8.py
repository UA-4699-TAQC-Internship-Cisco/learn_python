# -*- coding: utf-8 -*-


''' kata ky8 '''


import math


def litres(time):
    ''' kata https://www.codewars.com/kata/keep-hydrated-1'''
    if time > 0:
        return int(time*0.5)
    return u"Are you Christopher Nolan?"


def volume_of_a_rectangular_cuboid(length, width, height):
    '''kata https://www.codewars.com/kata/volume-of-a-cuboid'''
    if length > 0 and width > 0 and height > 0:
        return length*width*height
    return u"It is not a rectangular cuboid. Please check your data."


def convert_mpg_to_kpl(mpg):
    ''' kata https://www.codewars.com/kata/miles-per-gallon-to-kilometers-per-liter'''
    # 1 імперський галон = 4, 54609188 літра
    # 1 миля = 1, 609344 кілометра
    kilometres_per_litres = 1.609344/4.54609188
    result = mpg*kilometres_per_litres
    return round(result, 2)


def square_root_or_not(array):
    '''kata https://www.codewars.com/kata/to-square-root-or-not-to-square-root'''
    result = []
    for item in array:
        if int(item**0.5) == (item**0.5):
            result.append(int(item**0.5))
        result.append(int(item**2))
    return result


def count_positives_sum_negatives(array):
    '''kata https://www.codewars.com/kata/576bb71bbbcf0951d5000044'''
    if not array:
        return []
    positives_count = 0
    negatives_sum = 0
    for arr in array:
        if arr == 0:
            pass
        elif arr > 0:
            positives_count += 1
        elif arr < 0:
            negatives_sum += arr
    if positives_count == 0 and negatives_sum == 0:
        return []
    return [positives_count, negatives_sum]


def  convert_string_to_number(string):
    '''kata https://www.codewars.com/kata/convert-a-string-to-a-number'''
    return int(string)


def is_wilson_prime(p_n):
    '''kata https://www.codewars.com/kata/wilson-primes'''
    if p_n < 2:
        return False
    for i in range(2, int(p_n ** 0.5) + 1):
        if p_n % i == 0:
            return False

    numerator = math.factorial(p_n - 1) + 1
    denominator = p_n * p_n

    return numerator % denominator == 0


def formatting_decimal_places(num):
    '''kata https://www.codewars.com/kata/formatting-decimal-places-number-0'''
    return round(num, 2)


def  divisible_by_number(arr, num):
    '''kata https://www.codewars.com/kata/find-numbers-which-are-divisible-by-given-number'''
    result = []
    for item in arr:
        if item % num == 0:
            result.append(item)
    return result


