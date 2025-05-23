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


# Rainfall


def mean(town, strng):
    records = strng.split('\n')
    for record in records:
        if record.startswith(town + ":"):
            data = record.split(":")[1]
            pairs = data.split(",")
            values = [float(p.split()[1]) for p in pairs]
            return sum(values) / len(values)
    return -1


def variance(town, strng):
    mu = mean(town, strng)
    if mu == -1:
        return -1

    records = strng.split('\n')
    for record in records:
        if record.startswith(town + ":"):
            data = record.split(":")[1]
            pairs = data.split(",")
            values = [float(p.split()[1]) for p in pairs]
            return sum((x - mu) ** 2 for x in values) / len(values)
    return -1

# Ranking NBA teams


def nba_cup(result_sheet, to_find):
    if not to_find:
        return ""

    result_lines = result_sheet.split(",")
    W = D = L = Scored = Conceded = Points = 0
    played = False

    for match in result_lines:
        if re.search(r'\d+\.\d+', match):
            return f"Error(float number):{match}"

        match_re = re.match(r"(.+?) (\d+) (.+?) (\d+)$", match.strip())
        if not match_re:
            continue

        team1, score1, team2, score2 = match_re.groups()
        score1 = int(score1)
        score2 = int(score2)

        if to_find != team1 and to_find != team2:
            continue

        played = True

        if to_find == team1:
            Scored += score1
            Conceded += score2
            if score1 > score2:
                W += 1
                Points += 3
            elif score1 < score2:
                L += 1
            else:
                D += 1
                Points += 1
        elif to_find == team2:
            Scored += score2
            Conceded += score1
            if score2 > score1:
                W += 1
                Points += 3
            elif score2 < score1:
                L += 1
            else:
                D += 1
                Points += 1

    if not played:
        return f"{to_find}:This team didn't play!"

    return f"{to_find}:W={W};D={D};L={L};Scored={Scored};Conceded={Conceded};Points={Points}"


# Help the bookseller !


def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""

    category_sums = {}
    for cat in categories:
        category_sums[cat] = 0

    for item in stocklist:
        parts = item.split()
        code = parts[0]
        quantity = int(parts[1])
        category = code[0]

        if category in category_sums:
            category_sums[category] += quantity

    result_parts = []
    for cat in categories:
        part = "(" + cat + " : " + str(category_sums[cat]) + ")"
        result_parts.append(part)

    result = " - ".join(result_parts)
    return result

