from typing import NamedTuple


class Car(NamedTuple):
    color: str
    mileage: int
    gear: bool


car1 = Car('white', 12, True)
print(car1) # Car(color='white', mileage=12, gear=True)

car2 = Car(1, 'Black', False) # неправильно! Широкую на широкую!
print(car2)
