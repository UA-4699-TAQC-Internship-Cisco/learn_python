# -*- coding: utf-8 -*-

import math

def new_avg(arr, newavg): #Looking for a benefactor
    """The function return the expected donation that will permit to reach the average."""
    total_needed = newavg * (len(arr) + 1)

    next_donation = math.ceil(total_needed - sum(arr))

    if next_donation <= 0:
        raise ValueError("Expected donation must be more than 0.")

    return next_donation


def series_sum(number): #Sum of the first nth term of Series
    """Calculates the sum of all numbers in the series."""
    if number == 0:
        return "0.00"

    total = 0

    for i in range(number):
        total += 1.0 / (1 + 3 * i)

    return "{:.2f}".format(total)
