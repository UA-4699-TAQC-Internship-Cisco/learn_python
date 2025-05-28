def find_nb(m):
    total = 0
    n = 0
    while total < m:
        n += 1
        total += n ** 3
    return n if total == m else -1


def clean_line(line):
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789. ")
    return ''.join(ch for ch in line if ch in allowed)


def balance(book):
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


def f(x):
    return x / (((1 + x) ** 0.5) + 1)


def _extract_rain_data(data):
    lines = data.strip().split('\n')
    records = {}
    for line in lines:
        city, values = line.split(':')
        records[city] = [float(item.split()[1]) for item in values.split(',')]
    return records


def mean(town, data):
    records = _extract_rain_data(data)
    if town not in records:
        return -1
    nums = records[town]
    return sum(nums) / len(nums)


def variance(town, data):
    records = _extract_rain_data(data)
    if town not in records:
        return -1
    nums = records[town]
    m = sum(nums) / len(nums)
    return sum((x - m) ** 2 for x in nums) / len(nums)


def nba_cup(result_sheet, to_find):
    if not to_find:
        return ""

    games = [g for g in result_sheet.split(',') if to_find in g]
    if not games:
        return "{0}:This team didn't play!".format(to_find)

    w, d, l, scored, conceded, points = 0, 0, 0, 0, 0, 0

    for game in games:
        try:
            parts = game.strip().split()
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
            if len(scores) != 2:
                return "Error(float number):{0}".format(game)
            if to_find not in names:
                continue
            idx = names.index(to_find)
            opp = 1 - idx
            scored += scores[idx]
            conceded += scores[opp]
            if scores[idx] > scores[opp]:
                w += 1
                points += 3
            elif scores[idx] < scores[opp]:
                l += 1
            else:
                d += 1
                points += 1
        except (ValueError, IndexError):
            return "Error(float number):{0}".format(game)

    return "{0}:W={1};D={2};L={3};Scored={4};Conceded={5};Points={6}".format(
        to_find, w, d, l, scored, conceded, points
    )


def stock_list(lst, categories):
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
