var_str = input('Введите строку из нескольких слов\n')
str_list = var_str.split()
i = 0
while i < len(str_list):
    print('{0}). {1}'.format((i+1), str_list[i][0:10]))
    i += 1
