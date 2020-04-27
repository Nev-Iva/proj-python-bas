#5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import os

with open('txt files/my_hw5_5.txt', 'w') as file:
    while True:
        int_inp = input('Введите число (если вы хотите остановить ввод, введите stop): ')
        if int_inp.isdigit():
            file.write(int_inp + ' ')
        elif int_inp == 'stop':
            break
        else:
            print('Вы нужно ввести именно число')


with open('txt files/my_hw5_5.txt', 'r') as f:
    num_ls = f.read().split()
    sum_num = 0
    for el in num_ls:
        sum_num += int(el)
    print('Сумма чисел в файле равна: {0}'.format(sum_num))
