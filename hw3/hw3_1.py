def div_func(div_1, div_2):
    result = div_1 / div_2
    print(result)


while True:
    num_1 = input('Введите делимое')
    num_2 = input('Введите делитель')
    if num_1.isdigit() and num_2.isdigit():
        num_1 = int(num_1)
        num_2 = int(num_2)
        if num_2 == 0:
            print('На ноль делить нельзя. Делитель не может быть равен нулю')
        else:
            break

div_func(num_1, num_2)
