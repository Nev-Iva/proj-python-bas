name_1 = input('Введите название\n')
cost_1 = input('Введите цену\n')
num_1 = input('Введите количество\n')
un_1 = input('Введите единицу измерения\n')
inp_dict_1 = dict(Название=name_1, Цена=cost_1, Количество=num_1, Ед=un_1)

name_2 = input('Введите название\n')
cost_2 = input('Введите цену\n')
num_2 = input('Введите количество\n')
un_2 = input('Введите единицу измерения\n')
inp_dict_2 = dict(Название=name_2, Цена=cost_2, Количество=num_2, Ед=un_2)

name_3 = input('Введите название\n')
cost_3 = input('Введите цену\n')
num_3 = input('Введите количество\n')
un_3 = input('Введите единицу измерения\n')
inp_dict_3 = dict(Название=name_3, Цена=cost_3, Количество=num_3, Ед=un_3)

tup_1 = (1, inp_dict_1)
tup_2 = (2, inp_dict_2)
tup_3 = (3, inp_dict_3)
goods_list = [tup_1, tup_2, tup_3]
print(goods_list)

list_1 = [name_1, name_2, name_3]
list_2 = [cost_1, cost_2, cost_3]
list_3 = [num_1, num_2, num_3]
list_4 = [un_1, un_2, un_3]

inp_dict = dict(Название=list_1, Цена=list_2, Количество=list_3, Ед=list_4)
print(inp_dict)
