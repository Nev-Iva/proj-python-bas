inp_sec = int(input('введите время в секундах\n'))
var_hour = inp_sec // 3600
var_min = (inp_sec - var_hour * 3600) // 60
var_sec = inp_sec - var_hour * 3600 - var_min * 60
print('{0}:{1}:{2}'.format(var_hour, var_min, var_sec))