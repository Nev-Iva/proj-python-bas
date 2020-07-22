while True:
    res_1 = input('Введите результат первого дня\n')
    res_n = input('Введите желаемый результат\n')
    if res_1.isdigit() and res_n.isdigit():
        res_1 = int(res_1)
        res_n = int(res_n)
        break
    else:
        print('Ошибка ввода, введите число')
day = 1
while res_1 < res_n:
    res_1 *= 1.1
    day += 1
else:
    print('Спортсмен достигнет желаемого результата на {0} день'.format(day))
