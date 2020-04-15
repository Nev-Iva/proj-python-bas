while True:
    num = input('Введите число\n')
    if num.isdigit():
        break
    else:
        print('Ошибка ввода, введите число')

sum = int(num)+int(num*2)+int(num*3)
print(sum)

#2 способ
#while True:
#    num = input('Введите число\n')
#    if num.isdigit():
#        num = int(num)
#        break
#    else:
#        print('Ошибка ввода, введите число')
#
#sum = num+11*num+111*num
#print(sum)
