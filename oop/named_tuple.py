from collections import namedtuple

# Car = namedtuple('Авто', 'Цвет пробег')
Car = namedtuple('Авто', [
    'цвет',
    'пробег',
])

my_car = Car('Красный', 645316)
print(my_car)
print(my_car.цвет)
print(my_car.пробег)
print(my_car[0])
print(my_car[1])
print(tuple(my_car))

color, mileage = my_car
print(color, mileage)
print(*my_car)
class MyRedCar(Car):
    def body(self):
        if self.цвет == 'red':
            return 'sport'
        else:
            return 'van'

my_second_car = MyRedCar('red', 77)
print(my_second_car.body())

# расширение класса:
ElectricCar = namedtuple('ElectroCar', Car._fields + ('power',))
el_caro = ElectricCar('white', 134, 47)
print(el_caro)