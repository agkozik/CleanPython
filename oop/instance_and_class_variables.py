class Dog:
    num_legs = 4  # class

    def __init__(self, name):
        self.name = name  # instance


dog1 = Dog('DOG1')
dog2 = Dog('DOG2')

print(dog1.name, dog1.num_legs)
print(dog2.name, dog2.num_legs)

print(Dog.num_legs)

Dog.num_legs = 6
print(dog1.name, dog1.num_legs)
print(dog2.name, dog2.num_legs)

Dog.num_legs = 4
dog2.num_legs = 6

print(Dog.num_legs)
print(dog1.name, dog1.num_legs)
print(dog2.name, dog2.num_legs)
# теперь новая переменная экземпляра num_legs «оттеняет» переменную
# класса с тем же самым именем, переопределяя и скрывая ее, когда мы об-
# ращаемся к области действия экземпляра:
print(dog1.num_legs, dog1.__class__.num_legs)
print(dog2.num_legs, dog2.__class__.num_legs)  # стали несогласованными


# ----------------------------------------------------------
class Counter:
    increment = 3 # переменная класса

    def __init__(self):
        self.increment += 1 # ERROR! переменная экземпляра с тем же именем (increment)


class StaticCounter:
    increment2 = 0 # переменная класса

    def __init__(self):
        self.__class__.increment2 += 1 # CORRECT переменная класса


for i in range(0, 4):
    counter = Counter()
    staticCounter = StaticCounter()
    print('Counter =', counter.increment, counter.increment.__hash__(),
          ' Static Counter =', staticCounter.increment2, staticCounter.increment2.__hash__())

print(counter.increment)
print(staticCounter.increment)