def list_inf(**kwargs):
    return list(kwargs.values())


def get_inf():
   print(list_inf(name=input('Введите имя'),
         surname=input('Введите фамилию'),
         city=input('Введите ваш город'),
         email=input('Введите вашу почту'),
         phone=input('Введите ваш телефон')))


print(get_inf())
