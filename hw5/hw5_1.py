import os

with open('txt files/my_hw5_1.txt', 'w', encoding='UTF-8') as file:
    while True:
        inp_f = input('Что запишем в файл? (enter, если завершить запись) ')
        if inp_f == '':
            break
        else:
            file.write(inp_f + '\n')
