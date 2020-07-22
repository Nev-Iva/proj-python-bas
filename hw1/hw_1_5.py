while True:
    revenue = input('Введите выручку фирмы\n')
    cost = input('Введите издержки фирмы\n')
    if revenue.isdigit() and cost.isdigit():
        revenue = int(revenue)
        cost = int(cost)
        break
    else:
        print('Ошибка ввода, введите число')
profit = revenue - cost
if profit < 0:
    print('Фирма не рентабельна')
else:
    profitability = profit / revenue
    print('Фирма рентабельна, рентабельность составляет {0}'.format(profitability))
    while True:
        pop = input('Введите количество сотрудников фирмы\n')
        if pop.isdigit():
            pop = int(pop)
            break
        else:
            print('Ошибка ввода, введите число')
    per_emp = profit / pop
    print('Прибыль в фирме в расчете на одного сотрудника равна {0}'.format(per_emp))
