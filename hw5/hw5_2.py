import os

with open('txt files/my_hw5_2.txt', 'r', encoding='UTF-8') as file:
    str_line = file.read().splitlines()
    k = 1
    j = 0
    for i in str_line:
        i = i.split()
        j += len(i)
        print('В {0} строке {1} слов'.format(k, len(i)))
        k += 1

print('Всего в файле {0} строк и {1} слов'.format(len(str_line), j))
print(str_line)