# Build a pile of Cubes


import math
import re


def find_nb(m):
    x = math.isqrt(m)
    if x * x != m:
        return -1

    discriminant = 1 + 8 * x
    if discriminant < 0:
        return -1

    sqrt_discriminant = math.isqrt(discriminant)
    if sqrt_discriminant * sqrt_discriminant != discriminant:
        return -1

    n = (-1 + sqrt_discriminant) // 2

    if (n * (n + 1) // 2) ** 2 == m:
        return n
    else:
        return -1


# Easy Balance Checking


def balance(book):
    cleaned = re.sub(r"[^a-zA-Z0-9.\n ]+", "", book)
    lines = [line.strip() for line in cleaned.strip().split('\n') if line.strip()]
    original_balance = float(lines[0])
    balance = original_balance
    report = ["Original Balance: {:.2f}".format(balance)]
    total_expense = 0.0
    count = 0

    for line in lines[1:]:
        parts = line.split()
        check_number = parts[0]
        category = parts[1]
        amount = float(parts[2])
        balance -= amount
        total_expense += amount
        count += 1
        report.append("{} {} {:.2f} Balance {:.2f}".format(check_number, category, amount, balance))

    average_expense = total_expense / count if count else 0
    report.append("Total expense  {:.2f}".format(total_expense))
    report.append("Average expense  {:.2f}".format(average_expense))

    return "'\r\n'".join(report)

# Floating-point Approximation (I)


def f(x):
    return x / (math.sqrt(1 + x) + 1)





