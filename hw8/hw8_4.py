class WareHouse:

    def __init__(self, model_name, department, reg_num, count_num):
        self.model_name = model_name
        self.department = department
        self.reg_num = reg_num
        self.count_num = count_num

    def __str__(self):
        return 'Название модели: {0}, Отдел: {1}, Рег. номер: {2}, Кол-во: {3}'.format(self.model_name, self.department, self.reg_num, self.count_num)


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
