xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
shallow_copy = list(xs)
import copy

deep_copy = copy.deepcopy(xs)

print('original', xs)
print('shallow ', shallow_copy)
print('deep: ', deep_copy)
print('--------------------------------------')

xs[1][0] = 'X'
xs.append(['gjnhfm', 'fgfj'])
print('original', xs)
print('shallow ', shallow_copy)
print('deep: ', deep_copy)
print('--------------------------------------')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.x!r}, {self.y!r}'


point1 = Point(10, 20)
point2 = copy.copy(point1)
point3 = copy.deepcopy(point1)
print(point1 is point2)
print(point1 is point3)


class Rectan:
    def __init__(self, left_top, right_bottom):
        self.left_top = left_top
        self.right_bottom = right_bottom

    def __repr__(self):
        return (f'{self.__class__.__name__}({self.left_top!r},'
                f'{self.right_bottom!r})')


rect1 = Rectan(Point(1, 2), Point(3, 4))
rect2 = copy.copy(rect1)
rect3 = copy.deepcopy(rect1)
print(rect1)
print(rect2)
print(rect3)
print(rect2 is rect1)
print(rect3 is rect1)
rect1.left_top.x = 22
print(rect1)
print(rect2)
print(rect3)