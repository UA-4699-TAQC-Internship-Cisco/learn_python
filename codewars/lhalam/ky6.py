# -*- coding: utf-8 -*-

def find_nb(m): #Build a pile of Cubes
    suma = 0
    counter = 0
    i = 1
    while suma < m:
        suma += i ** 3
        counter += 1
        i += 1

    if suma == m:
        return counter

    return -1





def clean_line(line): #helper for balance
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789. ")
    cleaned = []
    for ch in line:
        if ch in allowed:
            cleaned.append(ch)
    return ''.join(cleaned)


def balance(book): #Easy Balance Checking
    l = [clean_line(line).strip() for line in book.splitlines() if line.strip() != '']

    start_balance = float(l[0])
    del l[0]

    l = [line.split(' ') for line in l if line.strip() != '']

    balance = start_balance
    total_expense = 0

    for elem in l:
        current_balance = balance - float(elem[-1])
        total_expense += float(elem[-1])

        elem.append("Balance")
        elem.append("{:.2f}".format(current_balance))

        balance = current_balance

    num_check = len(l)

    l.append(["Total_expense ", "{:.2f}".format(start_balance - balance)])
    l.append(["Average_expense ", "{:.2f}".format(total_expense / num_check)])

    l.insert(0, ["Original_Balance:", "{:.2f}".format(start_balance)])

    return "\r\n".join(" ".join(elem) for elem in l)


def f(x): #Floating-point Approximation (I)
    return x /((1+x)** 0.5 +1)



def mean(town, s):#Rainfall
    # your code
    d = {}

    for line in s.split('\n'):
        city, value = line.split(':')

        d[city] = value.split(',')
        gr = []

    for key, value in d.items():

        for e in value:
            t = e.split()

            gr.append(float(t[-1]))
        d[key] = sum(gr) / len(gr)
        gr = []

    if town not in d:
        return -1

    return d[town]


def variance(town, s):#Rainfall
    # your code
    d = {}

    for line in s.split('\n'):
        city, value = line.split(':')
        d[city] = value.split(',')

    gr = []
    for key, value in d.items():
        for e in value:
            t = e.split()
            gr.append(float(t[-1]))
        d[key] = gr
        gr = []

    if town not in d:
        return -1

    values = d[town]
    m = float(sum(values)) / len(values)
    var = sum((x - m) ** 2 for x in values) / float(len(values))
    return var


def nba_cup(result_sheet, to_find): #Ranking NBA teams
    if not to_find:
        return ""

    else:
        result = []
    for elem in result_sheet.split(','):
        if to_find in elem:
            result.append(elem)



    for i in range(len(result)):
        sublist = []
        parts = result[i].split(' ')
        team = []

        for part in parts:
            if part.isdigit():

                sublist.append((' '.join(team), int(part)))
                team = []
            else:
                team.append(part)

        result[i] = sublist

    w, l, d = 0, 0, 0

    s, c, p = 0, 0, 0

    for elem in result:
        if elem[0][-1] % 1 != 0 or elem[1][-1] % 1 != 0:
            return "Error(float number):" + ' '.join([team for team, score in elem])
        elif to_find in elem[0]:
            if elem[0][-1] > elem[1][-1]:
                w += 1
                p += 3
            elif elem[0][-1] < elem[1][-1]:
                l += 1
            elif elem[0][-1] == elem[1][-1]:
                d += 1
                p += 1
            s += elem[0][-1]
            c += elem[1][-1]
        elif to_find in elem[1]:
            if elem[0][-1] > elem[1][-1]:
                l += 1
            elif elem[0][-1] < elem[1][-1]:
                w += 1
                p += 3
            elif elem[0][-1] == elem[1][-1]:
                d += 1
                p += 1
            s += elem[1][-1]
            c += elem[0][-1]
        else:
            return "{}:This team didn't play!".format(to_find)

    return "{}:W={};D={};L={};Scored={};Conceded={};Points={}".format(to_find, w, d, l, s, c, p)






def stock_list(stocklist, categories): #Help the bookseller !
    # your code here
    if not stocklist or not categories:
        return ""

    book_dict = {cat: 0 for cat in categories}
    stocklist = [elem.split(',') for elem in stocklist]

    spl_stock = []

    for elem in stocklist:
        pairs = ' '.join(elem).split(' ')
        spl_stock.append(pairs)

    spl_stock = list(map(lambda x: [x[0][0], x[1]], spl_stock))

    for elem in spl_stock:
        cat, count = elem[0], int(elem[1])
        if cat in book_dict:
            book_dict[cat] += count

    result = []
    for cat in categories:
        result.append("({0} : {1})".format(cat, book_dict[cat]))

    return " - ".join(result)


