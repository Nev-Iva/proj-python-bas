import os
import re


with open('txt files/my_hw5_6.txt', 'r', encoding='UTF-8') as file:
    stud_ls = file.read().splitlines()

    dict_stud = {}
    for el in stud_ls:
        str_ls = el.split(': ')
        sum_st = 0
        num_st_ls = re.findall('(\d+)', str_ls[1])
        for k in num_st_ls:
            sum_st += int(k)
        dict_stud[str_ls[0]] = sum_st

print(dict_stud)



