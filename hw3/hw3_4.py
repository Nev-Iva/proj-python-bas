def my_func_1(x, y):
    y = abs(y)
    x = 1 / x**y
    return(x)


num_x = float(input('действительное положительное число x:\n'))
deg_y = int(input('целое отрицательное число y:\n'))
print(my_func_1(num_x, deg_y))


#2 способ


def my_func_2(x, y):
    y = abs(y)
    num_x = x
    i = 0
    while i < y-1:
        x *= num_x
        i += 1
    return 1 / x


num_x = float(input('действительное положительное число x:\n'))
deg_y = int(input('целое отрицательное число y:\n'))
print(my_func_1(num_x, deg_y))
