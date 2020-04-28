from collections import namedtuple
from sys import getsizeof

nt1 = namedtuple('Point', 'x, y, z')(1, 2, 3)
t2 = (1, 2, 3)
print(nt1)
print(getsizeof(nt1))

print(t2)
print(getsizeof(t2))

Car = namedtuple('Car', 'color mileage gear')
car1 = Car('red', 1111, 'auto')
print(car1) # Car(color='red', mileage=1111, gear='auto')
print(car1.color) # red