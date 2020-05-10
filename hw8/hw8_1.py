import datetime


class Data:
    def __init__(self, inp_date):
        self.inp_date = inp_date.split('.')

    @classmethod
    def format_date(cls, inp_date):
        try:
            day, month, year = [int(el) for el in inp_date.split('.')]
            format_date_type = '{0}\n{1}\n{2}'.format((type(day), day), (type(month), month), (type(year), year))
            return format_date_type
        except ValueError:
            return 'Некорректный формат даты.'

    @staticmethod
    def valid(inp_date):
        try:
            day, month, year = inp_date.split('.')
            datetime.date(int(year), int(month), int(day))
            return 'Корректный формат даты.'
        except ValueError:
            return 'Некорректный формат даты.'


date_1 = '05.03.2001'
date_2 = '01.02'
date_3 = '1423'
date_4 = '3.7.98'
print('Вы записали: {0}'.format(date_1))
print(Data.valid(date_1))
print('Вы записали: {0}'.format(date_2))
print(Data.format_date(date_2))
print('Вы записали: {0}'.format(date_3))
print(Data.format_date(date_3))
print('Вы записали: {0}'.format(date_4))
print(Data.valid(date_4))
