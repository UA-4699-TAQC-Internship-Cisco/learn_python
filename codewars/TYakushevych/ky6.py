# -*- coding: utf-8 -*-

def find_nb(number): #Build a pile of Cubes
    """Find number of cubes n """
    suma = 0
    counter = 0
    i = 1
    while suma < number:
        suma += i ** 3
        counter += 1
        i += 1

    if suma == number:
        return counter

    return -1





def clean_line(line): #helper for balance
    """Help to clean the line"""
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789. ")
    cleaned = []
    for char in line:
        if char in allowed:
            cleaned.append(char)
    return ''.join(cleaned)


def balance(book): #Easy Balance Checking
    """Clean balance sheet"""
    check_list = [clean_line(line).strip() for line in book.splitlines() if line.strip() != '']

    start_balance = float(check_list[0])
    del check_list[0]

    check_list = [line.split(' ') for line in check_list if line.strip() != '']

    current_expense = start_balance
    total_expense = 0

    for elem in check_list:
        current_balance = current_expense - float(elem[-1])
        total_expense += float(elem[-1])

        elem.append("Balance")
        elem.append("{:.2f}".format(current_balance))

        current_expense = current_balance

    num_check = len(check_list)

    check_list.append(["Total_expense ", "{:.2f}".format(start_balance - current_expense)])
    check_list.append(["Average_expense ", "{:.2f}".format(total_expense / num_check)])

    check_list.insert(0, ["Original_Balance:", "{:.2f}".format(start_balance)])

    return "\r\n".join(" ".join(elem) for elem in check_list)




def f(x): #Floating-point Approximation (I)
    """Return approximation  value"""
    return x /((1+x)** 0.5 +1)



def mean(town, s):#Rainfall
    """Calculate the mean rainfall of some town"""
    find_mean = {}

    for line in s.split('\n'):
        city, value = line.split(':')

        find_mean[city] = value.split(',')
        grader = []

    for key, value in find_mean.items():

        for elem in value:
            temperature = elem.split()

            grader.append(float(temperature[-1]))
        find_mean[key] = sum(grader) / len(grader)
        grader = []

    if town not in find_mean:
        return -1

    return find_mean[town]


def variance(town, s):#Rainfall
    """Calculate the variance of some town"""
    find_v = {}

    for line in s.split('\n'):
        city, value = line.split(':')
        find_v[city] = value.split(',')

    grader = []
    for key, value in find_v.items():
        for elem in value:
            temperature = elem.split()
            grader.append(float(temperature[-1]))
        find_v[key] = grader
        grader = []

    if town not in find_v:
        return -1

    values = find_v[town]
    average = float(sum(values)) / len(values)
    var = sum((x - average) ** 2 for x in values) / float(len(values))
    return var




def nba_cup(result_sheet, to_find): #Ranking NBA teams
    """Retuen NBA results for some team"""
    if not to_find:
        return ""

    else:
        result = []
    for elem in result_sheet.split(','):
        if to_find in elem:
            result.append(elem)

    for i, line in enumerate(result):
        sublist = []
        parts = line.split(' ')
        team = []

        for part in parts:
            if part.isdigit():
                sublist.append((' '.join(team), int(part)))
                team = []
            else:
                team.append(part)

        result[i] = sublist

    win, lose, draw = 0, 0, 0

    scored, conceded, points = 0, 0, 0

    for elem in result:
        if elem[0][-1] % 1 != 0 or elem[1][-1] % 1 != 0:
            return "Error(float number):" + ' '.join([team for team, score in elem])

        elif to_find in elem[0]:
            if elem[0][-1] > elem[1][-1]:
                win += 1
                points += 3

            elif elem[0][-1] < elem[1][-1]:
                lose += 1

            elif elem[0][-1] == elem[1][-1]:
                draw += 1
                points += 1

            scored += elem[0][-1]
            conceded += elem[1][-1]

        elif to_find in elem[1]:
            if elem[0][-1] > elem[1][-1]:
                lose += 1

            elif elem[0][-1] < elem[1][-1]:
                win += 1
                points += 3

            elif elem[0][-1] == elem[1][-1]:
                draw += 1
                points += 1

            scored += elem[1][-1]
            conceded += elem[0][-1]
        else:
            return "{}:This team didn't play!".format(to_find)

    return "{}:W={};D={};L={};Scored={};Conceded={};Points={}".format(
        to_find, win, draw, lose, scored, conceded, points)






def stock_list(stocklist, categories): #Help the bookseller !
    """Calculate the count of book for each category"""
    if not stocklist or not categories:
        return ""

    book_dict = {cat: 0 for cat in categories}
    stocklist = [elem.split(',') for elem in stocklist]

    spl_stock = []

    for elem in stocklist:
        pairs = ' '.join(elem).split(' ')
        spl_stock.append(pairs)

    spl_stock = [[x[0][0], x[1]] for x in spl_stock]


    for elem in spl_stock:
        cat, count = elem[0], int(elem[1])
        if cat in book_dict:
            book_dict[cat] += count

    result = []
    for cat in categories:
        result.append("({0} : {1})".format(cat, book_dict[cat]))

    return " - ".join(result)
