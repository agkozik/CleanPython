class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margarita(cls):
        return cls(['cheese', 'tomato'])

    @classmethod
    def sea_food_pizza(cls):
        return cls(['shrimp', 'olive', 'cheese'])


marg = Pizza.margarita()
sea = Pizza.sea_food_pizza()
print(marg)
print(sea)
print('----------------------------------------------------------------')
import math
class PizzaArea:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r},'
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

p = PizzaArea(30, ['shrimp', 'olive', 'cheese'])
print(p)
print(p.area())
print(p.circle_area(30))