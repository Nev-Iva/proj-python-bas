import os

dict_num = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('txt files/my_hw5_4.txt', 'r', encoding='UTF-8') as file:
    nums = file.read().splitlines()
    i = 0
    list_num_rus = []
    for el in nums:
        el = el.split(' — ')
        for key, value in dict_num.items():
            if el[0] == key:
                el[0] = value
                list_num_rus.append(el[0] + ' — ' + el[1])


with open('txt files/my_hw5_4_1.txt', 'w', encoding='utf-8') as f:
    for el in list_num_rus:
        f.write(el + '\n')
