def function(some_data, *args, **kwargs):
    print('Первый параметр: ', some_data)
    if args:
        print('Второй параметр: ', args)
    if kwargs:
        print('Третий параметр: ', kwargs)


function(1, 2, 'string', 4.0, id1='1', id2=2)

print('Модификация аргументов прежде чем передать их дальше:')


def bar(x, *args, **kwargs):
    print(x, args, kwargs)


def foo(x, *args, **kwargs):
    kwargs['имя'] = 'Sasha'
    new_args = args + ('дополнительное значение',)
    bar(x, *new_args, **kwargs)


foo('dsaf', 1, 2, k3=3, k4=4)

print('Расширение поведения родительского класса:')


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


class RedCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'red'


redCar = RedCar('green', 244000)
print(redCar.color)
