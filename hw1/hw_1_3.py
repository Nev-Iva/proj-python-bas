while True:
    num = input('Введите число\n')
    if num.isdigit():
        break
    else:
        print('Ошибка ввода, введите число')

sum_1 = int(num) + int(num * 2) + int(num * 3)
print(sum_1)

#while True:
#    num = input('Введите число\n')
#    if num.isdigit():
#        num = int(num)
#        break
#    else:
#        print('Ошибка ввода, введите число')
#sum_1 = num + 11 * num + 111 * num
#print(sum_1)
