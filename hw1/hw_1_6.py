a = int(input('Введите результат первого дня\n'))
b = int(input('Введите желаемый результат\n'))
day = 1
while a < b:
    a *= 1.1
    day += 1
else:
    print('Спортсмен достигнет желаемого результата на %d день' %day)