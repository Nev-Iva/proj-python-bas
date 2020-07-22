class DivZero(Exception):
    def __init__(self, pos_arg):
        self.pos_arg = pos_arg


def division(div_1, div_2):
    if div_2 == 0:
        raise DivZero('Невозможно деление на ноль')
    else:
        div_res = div_1 / div_2
        print('При делении {0} на {1} получилось {2}'.format(div_1, div_2, div_res))
    return div_1 / div_2


try:
    num_1 = int(input('Делимое\n'))
    num_2 = int(input('Делитель\n'))
    division(num_1, num_2)
except DivZero as pos_arg:
    print('{0}'.format(pos_arg))