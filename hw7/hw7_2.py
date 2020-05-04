from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, num):
        self.num = num

    @property
    def value_cloth(self):
        calc_cloth_price = self.num / 6.5 + 0.5 + 2 * self.num + 0.3
        return 'Стоимость ткани, необходимой для пошива составляет: {0}'.format(calc_cloth_price)

    @abstractmethod
    def abstract(self) -> float:
        pass


class Coat(Clothes):
    def value_cloth(self):
        calc_cloth_num = self.num / 6.5 + 0.5
        return 'Количество ткани, необходимое для кройки и пошива пальто: {0}'.format(calc_cloth_num)

    def abstract(self) -> float:
        pass


class Costume(Clothes):
    def value_cloth(self):
        calc_cloth_num = 2 * self.num + 0.3
        return 'Количество ткани, необходимое для кройки и пошива костюма: {0}'.format(calc_cloth_num)

    def abstract(self) -> float:
        pass


size_coat = int(input('Введите размер для пальто: '))
height_costume = int(input('Введите рост для костюма: '))
coat_red = Coat(size_coat)
costume_smoking = Costume(height_costume)
print(coat_red.value_cloth())
print(costume_smoking.value_cloth())

