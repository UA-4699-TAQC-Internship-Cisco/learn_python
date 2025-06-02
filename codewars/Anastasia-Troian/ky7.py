# -*- coding: utf-8 -*-

#10
def new_avg(arr, newavg):
    current_sum = sum(arr)
    n = len(arr)
    next_donation = int(newavg * (n + 1) - current_sum)

    if newavg * (n + 1) - current_sum > next_donation:
        next_donation += 1

    if next_donation <= 0:
        raise ValueError("Очікувана пожертва має бути позитивним числом.")

    return next_donation

#11
def series_sum(n):
    if n == 0:
        return "0.00"

    total = 0
    for i in range(n):
        total += 1.0 / (1 + i * 3)

    return "%.2f" % total
