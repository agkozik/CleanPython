class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # символ !r флаг преобразования для того, чтобы при вызове методов str(self.color) и str(self.mileage)
    # были использованы методы repr(self.color) и repr(self.mileage)
    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.color!r}, {self.mileage!r})')


# #дополнительно можно переопределить метод str
#     def __str__(self):
#         return f'{self.color}'


my_car = Car('dfhd', 4)
print(str(my_car))
print(repr(my_car))
