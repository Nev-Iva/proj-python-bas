while True:
    inp_sec = input('введите время в секундах\n')
    if inp_sec.isdigit():
        inp_sec = int(inp_sec)
        break
    else:
        print('Ошибка ввода, введите число')
var_hour = inp_sec // 3600
var_min = (inp_sec - var_hour * 3600) // 60
var_sec = inp_sec - var_hour * 3600 - var_min * 60
print('{0}:{1}:{2}'.format(var_hour, var_min, var_sec))
