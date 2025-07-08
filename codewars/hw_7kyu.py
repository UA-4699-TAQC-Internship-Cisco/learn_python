# Looking for a benefactor
import math


# Return the expected donation (rounded up to the next integer)
# that will permit to reach the average

def new_avg(donations, target_avg):
    required_total = target_avg * (len(donations) + 1)
    required_donation = math.ceil(required_total - sum(donations))

    if required_donation <= 0:
        raise ValueError("Required donation would be non-positive")
    return required_donation


# ================================================
# Sum of the first nth term of Series
def series_sum(term_count):
    """
    This module calculates the sum of the series:
    1 + 1/4 + 1/7 + 1/10 + ... up to the nth term.
    """
    if term_count == 0:
        return "0.00"
    total = sum(1.0 / (3 * i + 1) for i in range(term_count))
    return "{:.2f}".format(total)
