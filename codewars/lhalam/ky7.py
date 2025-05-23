# -*- coding: utf-8 -*-
import math

def looking_for_benefactor(donations, new_avg):
    required = (len(donations) + 1) * new_avg - sum(donations)
    if required <= 0:
        return u'result: variable, see "Sample Tests"'

    return "result: {num}".format(num = int(math.ceil(required)))


def series_sum(n):
    if n == 0:
        return "0.00"

    total = 0.0
    for i in range(n):
        total += 1.0 / (3 * i + 1)

    return round(total, 2)
