year_dict = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
while True:
    inp_month = input('введите номер месяца\n')
    if inp_month.isdigit():
        if (int(inp_month) >= 1) and (int(inp_month) <= 12):
            inp_month = int(inp_month)
            break
        else:
            print('Ошибка ввода, введите число от 1 до 12')
    else:
        print('Ошибка ввода, введите число')
for key, value in year_dict.items():
    if inp_month in year_dict[key]:
        print(key)
