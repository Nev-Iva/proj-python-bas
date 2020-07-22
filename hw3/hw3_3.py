def my_func(el_1, el_2, el_3):
    list_1 = [el_1, el_2, el_3]
    list_1.remove(min(el_1, el_2, el_3))
    print(sum(list_1))
    return sum(list_1)


while True:
    elem_1 = input('Введите первое число')
    elem_2 = input('Введите второе число')
    elem_3 = input('Введите третье число')
    if elem_1.isdigit() and elem_2.isdigit() and elem_3.isdigit():
        elem_1 = int(elem_1)
        elem_2 = int(elem_2)
        elem_3 = int(elem_3)
        break
    else:
        print('Введите числа')


my_func(elem_1, elem_2, elem_3)
