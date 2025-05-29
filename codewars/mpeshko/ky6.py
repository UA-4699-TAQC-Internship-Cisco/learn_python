# coding=utf-8
"""Auto-formatted with proper docstrings and Python 2.7 compatibility."""


def find_nb(value):
    """Find the number n such that 1³ + 2³ + ... + n³ = value, or return -1 if not possible."""
    total = 0
    number = 0
    while total < value:
        number += 1
        total += number ** 3
    return number if total == value else -1


def clean_line(line):
    """Remove all non-alphanumeric characters (except period and space) from the input string."""
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789. ")
    return ''.join(ch for ch in line if ch in allowed)


def balance(book):
    """Process a checkbook string and return cleaned, formatted balance summary."""
    lines = [clean_line(line).strip() for line in book.strip().splitlines() if line.strip()]
    start = float(lines[0])
    entries = [line.split() for line in lines[1:]]

    current = start
    total = 0
    formatted = []

    for entry in entries:
        amount = float(entry[-1])
        current -= amount
        total += amount
        formatted.append(" ".join(entry + ["Balance", "{0:.2f}".format(current)]))

    avg = total / len(entries)
    result = ["Original_Balance: {0:.2f}".format(start)] + formatted
    result.append("Total_expense  {0:.2f}".format(total))
    result.append("Average_expense  {0:.2f}".format(avg))

    return "\r\n".join(result)


def approx_expression(input_value):
    """Return result of expression: x / (sqrt(1 + x) + 1)."""
    return input_value / (((1 + input_value) ** 0.5) + 1)


def _extract_rain_data(data):
    """Extract city-wise rainfall data from a formatted multiline string."""
    lines = data.strip().split('\n')
    records = {}
    for line in lines:
        city, values = line.split(':')
        records[city] = [float(item.split()[1]) for item in values.split(',')]
    return records


def mean(town, data):
    """Return the mean monthly rainfall for a given town, or -1 if town not found."""
    records = _extract_rain_data(data)
    if town not in records:
        return -1
    nums = records[town]
    return sum(nums) / len(nums)


def variance(town, data):
    """Return the rainfall variance for a given town, or -1 if town not found."""
    records = _extract_rain_data(data)
    if town not in records:
        return -1
    nums = records[town]
    value = sum(nums) / len(nums)
    return sum((x - value) ** 2 for x in nums) / len(nums)


def parse_game_line(game_line):
    """Parse a game result line and return team names and scores."""
    parts = game_line.strip().split()
    scores = []
    names = []
    team = ""
    for part in parts:
        if part.replace('.', '', 1).isdigit():
            scores.append(int(float(part)))
            names.append(team.strip())
            team = ""
        else:
            team += part + " "
    return names, scores


def nba_cup(result_sheet, to_find):
    """Process basketball results and return stats for a given team."""
    if not to_find:
        return ""

    games = [g for g in result_sheet.split(',') if to_find in g]
    if not games:
        return "{0}:This team didn't play!".format(to_find)

    stats = {"wins": 0, "draws": 0, "losses": 0, "scored": 0, "conceded": 0, "points": 0}

    for game in games:
        try:
            names, scores = parse_game_line(game)
            if len(scores) != 2 or to_find not in names:
                return "Error(float number):{0}".format(game)
            idx = names.index(to_find)
            opp = 1 - idx
            stats["scored"] += scores[idx]
            stats["conceded"] += scores[opp]
            if scores[idx] > scores[opp]:
                stats["wins"] += 1
                stats["points"] += 3
            elif scores[idx] < scores[opp]:
                stats["losses"] += 1
            else:
                stats["draws"] += 1
                stats["points"] += 1
        except (ValueError, IndexError):
            return "Error(float number):{0}".format(game)

    return "{0}:W={1};D={2};L={3};Scored={4};Conceded={5};Points={6}".format(
        to_find, stats["wins"], stats["draws"], stats["losses"],
        stats["scored"], stats["conceded"], stats["points"]
    )


def stock_list(lst, categories):
    """Aggregate quantities of books by category and return formatted string."""
    if not lst or not categories:
        return ""
    totals = dict((c, 0) for c in categories)
    for item in lst:
        parts = item.split()
        cat = parts[0][0]
        qty = int(parts[1])
        if cat in totals:
            totals[cat] += qty
    return " - ".join("({0} : {1})".format(c, totals[c]) for c in categories)
