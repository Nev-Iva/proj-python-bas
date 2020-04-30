class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        str_full_name = 'Полное имя сотрудника: {0} {1}'.format(self.name, self.surname)
        return str_full_name

    def get_total_income(self):
        total_income = int(self._income['wage']) + int(self._income['bonus'])
        str_total_income = 'Доход с учетом премии: {0}'.format(total_income)
        return str_total_income

    def get_all_information(self):
        str_all_inf = '{0} {1} на должности {2} имеет доход {3} (+ дополнительно премия {4})'.format(self.name, self.surname, self.position, self._income['wage'], self._income['bonus'])
        return str_all_inf


worker1 = Position('Иван', 'Иванов', 'Слесарь 3-го разряда', '30000', '5000')
print(worker1.get_full_name())
print(worker1.get_total_income())
print(worker1.get_all_information())
print('\n')
worker2 = Position('Петр', 'Петров', 'Инженер-конструктор', '50000', '7000')
print(worker2.get_full_name())
print(worker2.get_total_income())
print(worker2.get_all_information())
