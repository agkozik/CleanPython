class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        else:
            self.count += 1
            return self.value


# def bounded_repeat(value, max_repeats):
#     count = 0
#     while True:
#         if count >= max_repeats:
#             return
#         count += 1
#         yield value

# упрощенная версия
def bounded_repeat(value, max_repeats):
    for i in range(max_repeats):
        yield value
        # в конец каждой функции Python добавляет неявную инструкцию
        # return None.


for x in bounded_repeat('hi', 3):
    print(x)
# --------------------------------------------------------------------------
generator = ('hello generator' for i in range(3))
print(generator)
# преобразовать в список:
print(list(generator))

# генераторы с фильтром:
even_squares = (x * x for x in range(10)
                if x % 2 == 0)
print(list(even_squares))