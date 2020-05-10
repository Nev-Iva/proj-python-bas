class WareHouse:

    def __init__(self, model_name, department, reg_num, count_num):
        self.model_name = model_name
        self.department = department
        self.reg_num = reg_num
        self.count_num = count_num
        self.items = {'Название модели': self.model_name,
                      'Отдел': self.department,
                      'Рег. номер': self.reg_num,
                      'Кол-во': self.count_num}

    def inp(self):
        try:
            model_name = str(input('Введите название модели устройства \n'))
            department = str(input('Введите отдел, к которому относится оргтехника \n '))
            reg_num = int(input('Введите регистрационный номер \n'))
            count_num = int(input('Введите количество моделей данного устройства \n'))
            dict_model = {'Название модели': model_name, 'Отдел': department, 'Рег. номер': reg_num, 'Кол-во': count_num}
            self.items.update(dict_model)
            print(self.items)
            return self.items
        except ValueError:
            print('Пожалуйста введите корректное значение для данного параметра.')


class Printer(WareHouse):
    pass


class Scanner(WareHouse):
    pass


class Xerox(WareHouse):
    pass


printer_1 = Printer('Canon i-SENSYS LBP623Cdw', 'Бухгалтерия', 78243849, 4)
scanner_1 = Scanner('CanoScan LiDE 400', 'Отдел кадров', 24234123, 2)
xerox_1 = Xerox('Xerox Phaser 3020BI', 'Отдел продаж', 1953072, 3)
print('{0}\n{1}\n{2}'.format(printer_1, xerox_1, scanner_1))
device_x = Printer('', '', 1, 1)
device_y = Scanner('', '', 1, 1)
device_z = Xerox('', '', 1, 1)
printer_2 = device_x.inp()
scanner_2 = device_y.inp()
xerox_2 = device_z.inp()
print('{0}\n{1}\n{2}'.format(printer_2, xerox_2, scanner_2))



