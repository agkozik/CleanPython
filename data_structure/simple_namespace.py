from types import SimpleNamespace

car1 = SimpleNamespace(color='red',
                       mileage=12,
                       gear=True
                       )

print(car1)
car1.color = 77
print(car1)
car1.damage = 'bumper'
print(car1)
