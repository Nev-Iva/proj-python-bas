import os

with open('txt files/my_hw5_3.txt', 'r', encoding='UTF-8') as file:
    nums = file.read().splitlines()
    sal_sum = 0
    num_emp = 0
    for i in nums:
        num_emp += 1
        i = i.split()
        sal_sum += int(i[1])
        if int(i[1]) < 20000:
            print('{0} имеет оклад менее 20 тыс.'.format(i[0]))
    av_sal = sal_sum / num_emp
    print('В фирме работает {0} сотрудников. Средняя зарплата по фирме составляет: {1} рублей.'.format(num_emp, av_sal))


