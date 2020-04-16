k = int(input('Введите количество элементов списка\n'))
var_str = []
for el in range(k):
    var_str.append(input('Введите элемент списка\n'))
print(var_str)
i = 0
for elem in range(int(len(var_str) / 2)):
    var_str[i], var_str[i + 1] = var_str[i + 1], var_str[i]
    i += 2
print(var_str)
