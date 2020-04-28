class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):  # Это вспомогательный класс, который нам нужно определить,
        # чтобы заработал наш пример итераций в цикле for…in:
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):  # связываем каждый экземпляр класса Repeater-
        #   Iterator с объектом Repeater, который его создал
        self.source = source

    def __next__(self):  # залезаем назад в «исходный» экземпляр класса Repeater и возвращаем связанное с ним значение
        return self.source.value


# repeater = Repeater('Hello')
# iterator = repeater.__iter__()
# while True:
#     item = iterator.__next__()
#     print(item)


repeater = Repeater('Hello')
for item in repeater:
    print(item)
