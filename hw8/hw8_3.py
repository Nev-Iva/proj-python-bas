class ExceptionType(Exception):
    def __init__(self, param):
        self.text = param


list_num = []


def num_check(el):
    if el.isdigit():
        list_num.append(el)
    else:
        raise ExceptionType('Необходимо ввести только число')


while True:
    el = input('Введите число (для выхода введите stop)\n')
    try:
        if el == 'stop':
            print(list_num)
            break
        else:
            num_check(el)
    except ExceptionType:
        print('Необходимо ввести только число')






