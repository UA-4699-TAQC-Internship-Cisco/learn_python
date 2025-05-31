# -*- coding: utf-8 -*-


''' kata ky6 '''


import math
import re


def find_nb(integer):
    '''kata https://www.codewars.com/kata/build-a-pile-of-cubes'''
    count, cubes = 1, 1
    while cubes < integer:
        count += 1
        cubes += count**3

    return count if integer == cubes else -1


def easy_balance_checking(txt):
    '''kata https://www.codewars.com/kata/easy-balance-checking'''
    txt_list = txt.split("\n")
    current_balance = float(txt_list[0])
    report = ""

    for element in txt_list:
        if element == txt_list[0]:
            report += "Original_Balance:_{e}\n".format(e=element)
        else:
            price = (element.split())[-1]
            current_balance -= float(price)
            report += element.replace(" ", "_") + "_Balance_" + str(current_balance) +"\n"

    expense = float(txt_list[0]) - current_balance
    report += "Total_expense__" + str(expense) +"\n"
    report += "Average_expense__" + str(expense/(len(txt_list)-1)) + "\n"
    return report


def floating_point_approximation(num):
    '''kata https://www.codewars.com/kata/floating-point-approximation-i'''
    return num / (math.sqrt(1 + num) + 1)


# Rainfall '''kata https://www.codewars.com/kata/rainfall'''
def parse_rainfall(town, strng):
    lines = strng.split('\n')
    for line in lines:
        if line.startswith(town + ":"):
            parts = line.split(":")[1]
            month_data = parts.split(",")
            values = [float(item.split(" ")[1]) for item in month_data]
            return values
    return None


def mean(town, strng):
    """Calculate mean rainfall for the town"""
    values = parse_rainfall(town, strng)
    if values is None:
        return -1.0
    return sum(values) / len(values)


def variance(town, strng):
    """Calculate variance of rainfall for the town"""
    values = parse_rainfall(town, strng)
    if values is None:
        return -1.0
    m = mean(town, strng)
    var = sum((x - m) ** 2 for x in values) / len(values)
    return var


def nba_cup(result_sheet, to_find):
    ''' kata https://www.codewars.com/kata/ranking-nba-teams'''
    if not to_find:
        return ""

    matches = result_sheet.split(',')
    stats = {'W': 0, 'D': 0, 'L': 0, 'Scored': 0, 'Conceded': 0, 'Points': 0}
    team_played = False

    for match in matches:
        if not to_find in match:
            continue
        if re.search(r'\d+\.\d+', match):
            return "Error(float number):" + match

        tokens = match.strip().split()
        scores = []
        teams = []
        temp = []
        for token in tokens:
            if token.isdigit():
                scores.append(int(token))
                teams.append(' '.join(temp))
                temp = []
            else:
                temp.append(token)

        if len(teams) != 2 or len(scores) != 2:
            continue  # skip invalid match format

        team1, team2 = teams
        score1, score2 = scores
        if to_find == team1 or to_find == team2:
            team_played = True
            if to_find == team1:
                scored = score1
                conceded = score2
            else:
                scored = score2
                conceded = score1

            stats['Scored'] += scored
            stats['Conceded'] += conceded
            if scored > conceded:
                stats['W'] += 1
                stats['Points'] += 3
            elif scored == conceded:
                stats['D'] += 1
                stats['Points'] += 1
            else:
                stats['L'] += 1

    if not team_played:
        return to_find + ":This team didn't play!"

    return ("%s:W=%d;D=%d;L=%d;Scored=%d;Conceded=%d;Points=%d" %
            (to_find, stats['W'], stats['D'], stats['L'],
             stats['Scored'], stats['Conceded'], stats['Points']))


def bookseller(stocklist, categories):
    '''kata https://www.codewars.com/kata/help-the-bookseller'''
    if not stocklist or not categories:
        return ""

    category_totals = {}
    for cat in categories:
        category_totals[cat] = 0

    for item in stocklist:
        code = item.split()[0]
        quantity = int(item.split()[1])
        if code[0] in category_totals:
            category_totals[code[0]] += quantity

    result = ["({cat} : {count})".format(cat=key, count=val)
              for key, val in category_totals.items()]
    return " - ".join(result)
