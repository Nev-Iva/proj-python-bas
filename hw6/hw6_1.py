import time


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def __running_light(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(1)
            i += 1

    def running(self):
        while True:
            self.__running_light()
            print('\nНовый цикл светофора\n')


trafficLight_1 = TrafficLight()
trafficLight_1.running()
