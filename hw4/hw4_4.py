old_list = [14, 9, 1, 2, 3, 5, 90, 14, 1, 2, 5, 90, 99, 32]
new_list = [el for el in old_list if old_list.count(el) == 1]
print('Исходный список: {0}'.format(old_list))
print('Результат получился: {0}'.format(new_list))
