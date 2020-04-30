class Road:
    _length = 0
    _width = 0

    def asph_calc(self, _width, _length, mass_per, depth):
        mass = (int(_width) * int(_length) * int(mass_per) * int(depth)) / 1000
        print('Для покрытия дороги длиной {0} и шириной {1} потребуется {2} тонн асфальта'.format(_length, _width, mass))


road_1 = Road()
road_1.asph_calc(30, 1000, 25, 5)
