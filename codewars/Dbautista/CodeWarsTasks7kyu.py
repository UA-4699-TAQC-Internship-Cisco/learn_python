# Looking for a benefactor

import math

def new_avg(arr, newavg):
    
    total = newavg * (len(arr) + 1)
    next_donation = math.ceil(total - sum(arr))
    
    if next_donation <= 0:
        raise ValueError("error")
    
    return next_donation

# Sum of the first nth term of Series

def series_sum(n):
    total = 0.0
    denominator = 1
    for _ in range(n):
        total += 1/denominator
        denominator += 3
    
    return f"{total:.2f}"



