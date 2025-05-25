# Build a pile of Cubes

def find_nb(m):
    total = 0
    n = 0
    while total < m:
        n += 1
        total += n ** 3
    return n if total == m else -1

# Easy Balance Checking

import re

def balance(book):

    lines = [re.sub(r'[^a-zA-Z0-9.\s]', '', line).strip() for line in book.strip().splitlines() if line.strip()]


    original_balance = float(lines[0])
    balance_now = original_balance

    result = [f"Original Balance: {format(original_balance, '.2f')}"]
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
        
        result.append(f"{check_number} {category} {format(amount, '.2f')} Balance {format(balance_now, '.2f')}")

    average_expense = total_expense / num_entries if num_entries else 0

    result.append(f"Total expense  {format(total_expense, '.2f')}")
    result.append(f"Average expense  {format(average_expense, '.2f')}")

    return "\r\n".join(result)


# Floating-point Approximation (I)

import math

def f(x):
    return x / (math.sqrt(1 + x) + 1)

# Rainfall

def parse_city_data(town, strng):
    for line in strng.split('\n'):
        if line.startswith(town + ":"):

            values = line.split(":")[1]
  
            rainfalls = [float(part.split()[1]) for part in values.split(",")]
            return rainfalls
    return None

def mean(town, strng):
    rainfalls = parse_city_data(town, strng)
    if rainfalls is None:
        return -1
    return sum(rainfalls) / len(rainfalls)

def variance(town, strng):
    rainfalls = parse_city_data(town, strng)
    if rainfalls is None:
        return -1
    m = mean(town, strng)
    return sum((x - m) ** 2 for x in rainfalls) / len(rainfalls)

# Ranking NBA teams

import re

def nba_cup(result_sheet, to_find):
    if not to_find:
        return ""

    w = d = l = scored = conceded = points = 0
    found = False

    games = result_sheet.split(',')

    for game in games:
        if not to_find in game:
            continue

        if re.search(r'\d+\.\d+', game):
            return f"Error(float number):{game}"


        nums = re.findall(r'\d+', game)
        if len(nums) < 2:
            continue


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
            s_for, s_against = score1, score2
        else:
            s_for, s_against = score2, score1

        scored += s_for
        conceded += s_against

        if s_for > s_against:
            w += 1
            points += 3
        elif s_for < s_against:
            l += 1
        else:
            d += 1
            points += 1

    if not found:
        return f"{to_find}:This team didn't play!"

    return f"{to_find}:W={w};D={d};L={l};Scored={scored};Conceded={conceded};Points={points}"


# Help the bookseller !

def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""

    totals = {cat: 0 for cat in categories}

    for item in stocklist:
        parts = item.split()
        code = parts[0]
        quantity = int(parts[1])
        category = code[0]

        if category in totals:
            totals[category] += quantity

    return " - ".join(f"({cat} : {totals[cat]})" for cat in categories)
