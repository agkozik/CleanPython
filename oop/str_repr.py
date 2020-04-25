class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'цвет авто: {self.color}, пробег {self.mileage} __str__'

    def __repr__(self):
        return f'цвет авто: {self.color}, пробег {self.mileage} __repr__'


my_red_car = Car('красный', 7)
print(my_red_car)
# если написать в консоли интерпретатора my_red_car тогда обращение к методу __repr__

print('\nЛучше использовать встроенные методы str() и repr()')
print(str(my_red_car))
print(repr(my_red_car))

import  datetime
today =datetime.date.today()
print(str(today), ' это __str__')
print(repr(today), 'это __repr__')