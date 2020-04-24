class Adder:
    def __init__(self, number):
        self.number = number

    def __call__(self, x):
        return self.number + x


adder = Adder(3)
print(adder(10))
print(Adder(1)(2))
# проверка, является ли объект или функция вызываемыми
print(callable(adder))