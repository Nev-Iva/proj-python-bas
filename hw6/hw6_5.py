class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def start_draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Запуск отрисовки {0}'.format(self.title)


class Pencil(Stationery):
    def draw(self):
        return 'Запуск отрисовки {0}'.format(self.title)


class Handle(Stationery):
    def draw(self):
        return 'Запуск отрисовки {0}'.format(self.title)


pen1 = Pen('Ручкой')
print(pen1.draw())
print('\n')
pencil2 = Pencil('Карандашом')
print(pencil2.draw())
print('\n')
handle3 = Handle('Маркером')
print(handle3.draw())