# Looking for a benefactor


import math


def new_avg(arr, newavg):
    arr_len = len(arr)
    sum_arr = sum(arr)
    result = newavg * (arr_len + 1) - sum_arr
    if result <= 0:
        raise ValueError("Error")
    return math.ceil(result)
