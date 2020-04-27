import os
import json

with open('txt files/my_hw5_7.txt', 'r') as file:
    firms = file.read().splitlines()
    dict_firms = {}
    dict_av = {}
    i = 0
    prof_sum = 0
    ls_firm_av = []
    for el in firms:
        firm_doc = el.split()
        profit = int(firm_doc[2]) - int(firm_doc[3])
        dict_firms[firm_doc[0]] = profit
        if profit > 0:
            prof_sum += profit
            i += 1
        else:
            print('Фирма {0} терпит убытки, убытки составили {1}'.format(firm_doc[0], abs(profit)))
    average_profit = round((prof_sum / i), 2)
    dict_av['average_profit'] = average_profit
    ls_firm_av.append(dict_firms)
    ls_firm_av.append(dict_av)
    print(ls_firm_av)

json_firms = json.dumps(ls_firm_av)
print(json_firms)