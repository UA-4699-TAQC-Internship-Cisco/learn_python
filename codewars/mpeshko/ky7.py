import math

def new_avg(arr, newavg):
    total = newavg * (len(arr) + 1)
    donation = int(math.ceil(total - sum(arr)))
    if donation <= 0:
        raise ValueError("Expected donation must be more than 0.")
    return donation


def series_sum(n):
    if n == 0:
        return "0.00"
    total = 0.0
    for i in range(n):
        total += 1.0 / (1 + 3 * i)
    return "{0:.2f}".format(total)
