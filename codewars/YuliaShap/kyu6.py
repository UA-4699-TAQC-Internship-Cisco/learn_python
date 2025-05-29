# Build a pile of Cubes


import math
import re


def find_nb(target_volume):
    sqrt_volume = int(math.sqrt(target_volume))
    if sqrt_volume * sqrt_volume != target_volume:
        return -1

    discriminant = 1 + 8 * sqrt_volume
    if discriminant < 0:
        return -1

    sqrt_discriminant = int(math.sqrt(discriminant))
    if sqrt_discriminant * sqrt_discriminant != discriminant:
        return -1

    number_of_cubes = (-1 + sqrt_discriminant) // 2

    if (number_of_cubes * (number_of_cubes + 1) // 2) ** 2 == target_volume:
        return number_of_cubes
    return -1


# Easy Balance Checking


def balance(book):
    cleaned = re.sub(r"[^a-zA-Z0-9.\n ]+", "", book)
    lines = [line.strip() for line in cleaned.strip().split('\n') if line.strip()]
    original_balance = float(lines[0])
    current_balance = original_balance
    report = ["Original Balance: {:.2f}".format(current_balance)]
    total_expense = 0.0
    count = 0

    for line in lines[1:]:
        parts = line.split()
        check_number = parts[0]
        category = parts[1]
        amount = float(parts[2])
        current_balance -= amount
        total_expense += amount
        count += 1
        report.append("{} {} {:.2f} Balance {:.2f}".format(check_number, category, amount, balance))

    average_expense = total_expense / count if count else 0
    report.append("Total expense  {:.2f}".format(total_expense))
    report.append("Average expense  {:.2f}".format(average_expense))

    return "'\r\n'".join(report)


# Floating-point Approximation (I)


def floating(number):
    return number / (math.sqrt(1 + number) + 1)


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
    result = mean(town, strng)
    if result == -1:
        return -1

    records = strng.split('\n')
    for record in records:
        if record.startswith(town + ":"):
            data = record.split(":")[1]
            pairs = data.split(",")
            values = [float(p.split()[1]) for p in pairs]
            return sum((x - result) ** 2 for x in values) / len(values)
    return -1


# Ranking NBA teams


def nba_cup(result_sheet, to_find):
    if not to_find:
        return ""

    result_lines = result_sheet.split(",")
    stats = {
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "scored": 0,
        "conceded": 0,
        "points": 0
    }
    played = False

    for match in result_lines:
        if re.search(r'\d+\.\d+', match):
            return "Error(float number):{}".format(match)

        match_re = re.match(r"(.+?) (\d+) (.+?) (\d+)$", match.strip())
        if not match_re:
            continue

        team1, score1, team2, score2 = match_re.groups()
        score1 = int(score1)
        score2 = int(score2)

        if to_find != team1 and to_find != team2:
            continue

        played = True
        is_team1 = (to_find == team1)

        team_score = score1 if is_team1 else score2
        opponent_score = score2 if is_team1 else score1

        stats["scored"] += team_score
        stats["conceded"] += opponent_score

        if team_score > opponent_score:
            stats["wins"] += 1
            stats["points"] += 3
        elif team_score < opponent_score:
            stats["losses"] += 1
        else:
            stats["draws"] += 1
            stats["points"] += 1

    if not played:
        return "{}:This team didn't play!".format(to_find)

    return (
        "{}:W={};D={};L={};Scored={};Conceded={};Points={}".format(
            to_find,
            stats["wins"],
            stats["draws"],
            stats["losses"],
            stats["scored"],
            stats["conceded"],
            stats["points"]
        )
    )

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
