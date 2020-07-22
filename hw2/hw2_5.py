my_list = [7, 5, 3, 3, 2]
while True:
    while True:
        new_el = input('Введите новый элемент\n')
        if new_el.isdigit():
            new_el = int(new_el)
            break
        else:
            print('Введите элемент-число')
    my_list.append(new_el)
    my_list_2 = sorted(my_list, reverse=True)
    print(my_list_2)
