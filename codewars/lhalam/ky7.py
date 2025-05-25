# -*- coding: utf-8 -*-

import math

def new_avg(arr, newavg): #Looking for a benefactor
    total_needed = newavg * (len(arr) + 1)

    next_donation = math.ceil(total_needed - sum(arr))

    if next_donation <= 0:
        raise ValueError("Expected donation must be more than 0.")

    return next_donation


def series_sum(n): #Sum of the first nth term of Series
    # Happy Coding ^_^
    if n == 0:
        return "0.00"

    total = 0

    for i in range(n):
        total += 1.0 / (1 + 3 * i)

    return "{:.2f}".format(total)