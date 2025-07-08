import math


# ================================================
# Build a pile of Cubes
def find_nb(total_volume):
    """Calculate the number of cubes needed to reach a total volume."""
    current_sum = 0
    cube_count = 1
    while current_sum < total_volume:
        current_sum += cube_count ** 3
        cube_count += 1
    return cube_count - 1 if current_sum == total_volume else -1


# ================================================
# Easy Balance Checking
def balance(book):
    chars = "!=:;-_+^/(){}?*'%&@,;$#€"

    for c in chars:
        if c in book:
            book = book.replace(c, "")

    lines = book.split("\n")
    balance, total, expense, last = None, 0, 0, []

    for e, i in enumerate(lines):
        if len(i) == 0:
            continue
        elif e == 0:
            balance = float(i)
            last.append("Original Balance: {:.2f}".format(balance))
        else:
            data = i.split(" ")
            amount = float(data[2])
            total += amount
            last.append(
                "{} {} {:.2f} Balance {:.2f}".format(data[0], data[1], float(data[2]), round(balance - amount, 2)))
            balance -= amount
            expense += 1

    average = round(total / expense, 2)
    last.append("Total expense  {:.2f}".format(round(total, 2)))
    last.append("Average expense  {:.2f}".format(average))
    return "\r\n".join(last)


# ================================================
# Floating-point Approximation (I)
def precise_calculation(small_x):
    """
    Module providing a precise calculation for sqrt(1 + x) - 1 when x is near 0.
    """
    return small_x / (math.sqrt(1 + small_x) + 1)


# ================================================
# Rainfall
def mean(town, rainfall_string):
    rainfall_data = extract_rainfall_data(town, rainfall_string)
    if not rainfall_data:
        return -1.0
    return sum(rainfall_data) / len(rainfall_data)


def variance(town, rainfall_string):
    rainfall_data = extract_rainfall_data(town, rainfall_string)
    if not rainfall_data:
        return -1.0
    average = sum(rainfall_data) / len(rainfall_data)
    squared_diffs = [(value - average) ** 2 for value in rainfall_data]
    return sum(squared_diffs) / len(squared_diffs)


def extract_rainfall_data(town, rainfall_string):
    if not rainfall_string:
        return []

    for line in rainfall_string.split('\n'):
        parts = line.split(':')
        if parts[0] == town:
            monthly_data = parts[1].split(',')
            rainfall_values = []
            for entry in monthly_data:
                try:
                    value = float(entry.split()[1])
                    rainfall_values.append(value)
                except (IndexError, ValueError):
                    continue
            return rainfall_values if rainfall_values else []
    return []


# ================================================
# Ranking NBA teams
def nba_cup(result_sheet, to_find):
    """
    NBA Team Ranking System
    """
    if not to_find:
        return ""

    matches = result_sheet.split(',') if result_sheet else []
    stats = {
        'W': 0,  # Wins
        'D': 0,  # Draws
        'L': 0,  # Losses
        'Scored': 0,  # Total points scored
        'Conceded': 0,  # Total points conceded
        'Points': 0  # Ranking points
    }

    for match in matches:
        match = match.strip()
        if not match:
            continue

        # Check for float numbers in scores
        if any(has_float_score(part) for part in match.split()):
            return "Error(float number):{0}".format(match)

        # Parse the match data
        try:
            team1, score1, team2, score2 = parse_match(match)
        except (ValueError, IndexError):
            continue  # Skip invalid match formats

        # Update statistics if the team played in this match
        update_stats(stats, to_find, team1, team2, score1, score2)

    return format_result(to_find, stats)


def has_float_score(part):
    """Check if a string part represents a float score."""
    try:
        float_num = float(part)
        return not float_num.is_integer()
    except ValueError:
        return False


def parse_match(match_str):
    """Parse a match string into team and score components."""
    parts = match_str.split()
    # Find the index where scores appear
    score_indices = [i for i, part in enumerate(parts) if part.isdigit()]

    if len(score_indices) < 2:
        raise ValueError("Invalid match format")

    score1_idx = score_indices[0]
    score2_idx = score_indices[1]

    team1 = ' '.join(parts[:score1_idx])
    score1 = int(parts[score1_idx])
    team2 = ' '.join(parts[score1_idx + 1:score2_idx])
    score2 = int(parts[score2_idx])

    return team1, score1, team2, score2


def update_stats(stats, team_name, team1, team2, score1, score2):
    """Update statistics based on match results."""
    if team_name not in (team1, team2):
        return

    if team1 == team_name:
        scored = score1
        conceded = score2
        if score1 > score2:
            result = 'W'
            points = 3
        elif score1 == score2:
            result = 'D'
            points = 1
        else:
            result = 'L'
            points = 0
    else:
        scored = score2
        conceded = score1
        if score2 > score1:
            result = 'W'
            points = 3
        elif score2 == score1:
            result = 'D'
            points = 1
        else:
            result = 'L'
            points = 0

    stats['Scored'] += scored
    stats['Conceded'] += conceded
    stats[result] += 1
    stats['Points'] += points


def format_result(team_name, stats):
    """Format the results into the required output string."""
    if stats['W'] == 0 and stats['D'] == 0 and stats['L'] == 0:
        return "{0}:This team didn't play!".format(team_name)

    return (
        "{0}:W={1};D={2};L={3};Scored={4};Conceded={5};Points={6}".format(
            team_name,
            stats['W'],
            stats['D'],
            stats['L'],
            stats['Scored'],
            stats['Conceded'],
            stats['Points']
        )
    )


# ================================================
# Help the bookseller !
def stock_list(stock_list, categories):
    """
    Calculate book quantities by category from stocklist.
    """
    if not stock_list or not categories:
        return ""

    totals = dict((category, 0) for category in categories)

    for item in stock_list:
        parts = item.split()
        if len(parts) < 2:
            continue
        code = parts[0]
        quantity = parts[1]
        if not code or not quantity:
            continue
        category = code[0] if code else ''
        try:
            qty = int(quantity)
        except ValueError:
            continue
        if category in totals:
            totals[category] += qty

    result_parts = []
    for category in categories:
        result_parts.append("({0} : {1})".format(category, totals[category]))
    return " - ".join(result_parts)
