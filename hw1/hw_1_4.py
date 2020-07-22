while True:
    num_str = input('Введите целое положительное число\n')
    if num_str.isdigit():
        break
    else:
        print('Ошибка ввода, введите число')
i = 0
max_num = 0
while i < len(num_str):
    if int(num_str[i]) > max_num:
        max_num = int(num_str[i])
        i += 1
    else:
        i += 1
print('Наибольшая цифра в числе {0} ---> {1}'.format(num_str, max_num))
