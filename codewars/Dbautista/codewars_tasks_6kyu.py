import math
import re


def find_nb(m):
    """Find number of cubes n such that 1^3 + 2^3 + ... + n^3 = m"""
    total = 0
    n = 0
    while total < m:
        n += 1
        total += n ** 3
    return n if total == m else -1


def balance(book):
    """Clean and compute balance sheet"""
    lines = [
        re.sub(r'[^a-zA-Z0-9.\s]', '', line).strip()
        for line in book.strip().splitlines() if line.strip()
    ]

    original_balance = float(lines[0])
    balance_now = original_balance

    result = ["Original Balance: %.2f" % original_balance]
    total_expense = 0.0
    num_entries = 0

    for line in lines[1:]:
        parts = line.split()
        check_number = parts[0]
        category = parts[1]
        amount = float(parts[2])

        balance_now -= amount
        total_expense += amount
        num_entries += 1

        result.append(
            "%s %s %.2f Balance %.2f" % (check_number, category, amount, balance_now)
        )

    average_expense = total_expense / num_entries if num_entries else 0

    result.append("Total expense  %.2f" % total_expense)
    result.append("Average expense  %.2f" % average_expense)

    return "\r\n".join(result)


def f(x):
    """Return approximation function value"""
    return x / (math.sqrt(1 + x) + 1)


def parse_city_data(town, strng):
    """Extract rainfall data for a specific town"""
    for line in strng.split('\n'):
        if line.startswith(town + ":"):
            values = line.split(":")[1]
            rainfalls = [float(part.split()[1]) for part in values.split(",")]
            return rainfalls
    return None


def mean(town, strng):
    """Calculate mean rainfall for the town"""
    rainfalls = parse_city_data(town, strng)
    if rainfalls is None:
        return -1
    return sum(rainfalls) / len(rainfalls)


def variance(town, strng):
    """Calculate variance of rainfall for the town"""
    rainfalls = parse_city_data(town, strng)
    if rainfalls is None:
        return -1
    mean_value = mean(town, strng)
    return sum((x - mean_value) ** 2 for x in rainfalls) / len(rainfalls)


def nba_cup(result_sheet, to_find):
    """Return NBA stats for the given team"""
    if not to_find:
        return ""

    wins = draws = losses = scored = conceded = points = 0
    found = False

    games = result_sheet.split(',')

    for game in games:
        if to_find not in game:
            continue

        if re.search(r'\d+\.\d+', game):
            return "Error(float number):%s" % game

        match = re.match(r'^(.*) (\d+) (.*) (\d+)$', game.strip())
        if not match:
            continue

        team1 = match.group(1).strip()
        score1 = int(match.group(2))
        team2 = match.group(3).strip()
        score2 = int(match.group(4))

        if to_find != team1 and to_find != team2:
            continue

        found = True

        if to_find == team1:
            score_for, score_against = score1, score2
        else:
            score_for, score_against = score2, score1

        scored += score_for
        conceded += score_against

        if score_for > score_against:
            wins += 1
            points += 3
        elif score_for < score_against:
            losses += 1
        else:
            draws += 1
            points += 1

    if not found:
        return "%s:This team didn't play!" % to_find

    return (
        "%s:W=%d;D=%d;L=%d;Scored=%d;Conceded=%d;Points=%d"
        % (to_find, wins, draws, losses, scored, conceded, points)
    )


def stock_list(stocklist, categories):
    """Summarize stock by book categories"""
    if not stocklist or not categories:
        return ""

    totals = dict((cat, 0) for cat in categories)

    for item in stocklist:
        parts = item.split()
        code = parts[0]
        quantity = int(parts[1])
        category = code[0]

        if category in totals:
            totals[category] += quantity

    return " - ".join("( %s : %d )" % (cat, totals[cat]) for cat in categories)
