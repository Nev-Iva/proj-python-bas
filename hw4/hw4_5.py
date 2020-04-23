import functools

list_num = []
list_num = [el for el in range(100, 1001) if el % 2 == 0]
print(list_num)
print(functools.reduce(lambda x, y: x * y, list_num))
