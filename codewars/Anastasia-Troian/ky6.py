#12
def find_nb(m):
    n = 0
    total = 0
    while total < m:
        n += 1
        total += n ** 3

    return n if total == m else -1

#13
def balance(book):
    lines = book.split('\n')

    def clean_line(line):
        allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789. "
        cleaned = ""
        for ch in line:
            if ch in allowed_chars:
                cleaned += ch
        return cleaned

    cleaned_lines = [clean_line(line) for line in lines if line.strip() != '']

    balance = float(cleaned_lines[0])
    result_lines = ["Original Balance: {:.2f}".format(balance)]

    total_expense = 0.0
    count = 0

    for line in cleaned_lines[1:]:
        parts = line.split()
        if len(parts) < 2:
            continue

        check_number = parts[0]
        amount_str = parts[-1]
        try:
            amount = float(amount_str)
        except ValueError:
            continue

        category = ' '.join(parts[1:-1]) if len(parts) > 2 else ''

        total_expense += amount
        balance -= amount
        count += 1

        result_lines.append("{} {} {:.2f} Balance {:.2f}".format(check_number, category, amount, balance))

    average_expense = total_expense / count if count else 0.0

    result_lines.append("Total expense  {:.2f}".format(total_expense))
    result_lines.append("Average expense  {:.2f}".format(average_expense))

    return '\r\n'.join(result_lines)

#14
def f(x):
    return x / ( (1 + x)**0.5 + 1 )

#15
def mean(town, s):
    lines = s.split('\n')
    for line in lines:
        if line.startswith(town + ":"):
            data_part = line.split(':')[1]
            pairs = data_part.split(',')
            values = []
            for pair in pairs:
                try:
                    value = float(pair.split()[1])
                    values.append(value)
                except:
                    pass
            if not values:
                return -1
            return sum(values) / len(values)
    return -1

def variance(town, s):
    avg = mean(town, s)
    if avg == -1:
        return -1
    lines = s.split('\n')
    for line in lines:
        if line.startswith(town + ":"):
            data_part = line.split(':')[1]
            pairs = data_part.split(',')
            values = []
            for pair in pairs:
                try:
                    value = float(pair.split()[1])
                    values.append(value)
                except:
                    pass
            if not values:
                return -1
            n = len(values)
            var = sum((x - avg) ** 2 for x in values) / n
            return var
    return -1

#16
def nba_cup(result_sheet, to_find):
    if to_find == "":
        return ""

    matches = result_sheet.split(',')
    W = D = L = scored = conceded = points = 0
    played = False

    for match in matches:
        match = match.strip()
        if match == "":
            continue

        parts = match.split()

        score_indices = []
        for i, part in enumerate(parts):
            try:
                float_part = float(part)
                if '.' in part:
                    return "Error(float number):" + match
                score_indices.append(i)
            except:
                continue

        if len(score_indices) != 2:
            continue

        idx1, idx2 = score_indices
        score1 = int(parts[idx1])
        score2 = int(parts[idx2])

        team1 = " ".join(parts[:idx1])
        team2 = " ".join(parts[idx1 + 1:idx2])

        if to_find == team1 or to_find == team2:
            played = True
            if to_find == team1:
                scored += score1
                conceded += score2
                if score1 > score2:
                    W += 1
                    points += 3
                elif score1 == score2:
                    D += 1
                    points += 1
                else:
                    L += 1
            else:
                scored += score2
                conceded += score1
                if score2 > score1:
                    W += 1
                    points += 3
                elif score2 == score1:
                    D += 1
                    points += 1
                else:
                    L += 1

    if not played:
        return to_find + ":This team didn't play!"

    return ("%s:W=%d;D=%d;L=%d;Scored=%d;Conceded=%d;Points=%d" %
            (to_find, W, D, L, scored, conceded, points))

#17
def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""

    category_counts = {cat: 0 for cat in categories}

    for book in stocklist:
        category = book[0]
        quantity = int(book.split()[1])

        if category in category_counts:
            category_counts[category] += quantity

    result = " - ".join("(%s : %d)" % (cat, category_counts[cat]) for cat in categories)
    return result