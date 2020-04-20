def str_func():
    str_sum = 0
    while True:
        str_num = input('Введите числа через пробел или спец знак стоп(st)')
        str_num = str_num.split()
        for el in str_num:
            try:
                if el == 'st':
                    print('Сумма чисел в строке составляет {0}.'.format(str_sum))
                    return
                else:
                    str_sum += int(el)
            except ValueError:
                print('Введите число или спец знак (st)')
        print('Сумма чисел в строке {0}'.format(str_sum))


print(str_func())
