from sys import argv
_, prod, sal_per_hour, prize = argv

print('Выработка в часах: {0}'.format(prod))
print('Ставка в час: {0}'.format(sal_per_hour))
print('Премия: {0}'.format(prize))
res_sal = int(prod) * int(sal_per_hour) + int(prize)
print('Заработная плата сотрудника составляет: {0}'.format(res_sal))
