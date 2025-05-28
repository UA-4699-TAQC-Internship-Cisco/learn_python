import math

def new_avg(arr, new_avg):
    """
    Calculate the minimum next donation needed to reach the new average.
    """
    total = new_avg * (len(arr) + 1)
    next_donation = math.ceil(total - sum(arr))

    if next_donation <= 0:
        raise ValueError("error")

    return next_donation


def series_sum(num_terms):
    """
    Calculate the sum of the first n terms of the series: 1 + 1/4 + 1/7 + 1/10 + ...
    """
    total = 0.0
    denominator = 1
    for _ in range(num_terms):
        total += 1.0 / denominator
        denominator += 3

    return "{0:.2f}".format(total)
