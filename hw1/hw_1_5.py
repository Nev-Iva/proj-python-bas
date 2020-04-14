revenue = int(input('Введите выручку фирмы\n'))
cost = int(input('Введите издержки фирмы\n'))
profit = revenue - cost
if profit < 0:
    print('Фирма не рентабельна')
else:
    profitability = profit / revenue
    print('Фирма рентабельна, рентабельность составляет %f' %profitability)
    pop = int(input('Введите количество сотрудников фирмы\n'))
    per_emp = profit / pop
    print('Прибыль в фирме в расчете на одного сотрудника равна %f'%per_emp)