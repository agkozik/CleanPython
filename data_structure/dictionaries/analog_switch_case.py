def func_1(a, b):
    return a + b


def func_2(a, b):
    return a - b


def func_3(a, b):
    return a * b


def func_4(a, b):
    return a / b


def func_def(a, b):
    return "Некорректное значение"


dict_of_func = {
    'add': func_1,
    'sub': func_2,
    'mult': func_3,
    'div': func_4,
}

operation = 'zdf'
# print(dict_of_func[operation](10, 5)) # не поддерживается некорректный ввод


print(dict_of_func.get(operation, func_def)(10, 5))  # поддержка блока default (некорректный ввод)


# --------------------------упрощенная реализация НО всякий раз, когда мы вызываем dispatch_dict(), он создает
# временный словарь и кучу лямбд для поиска кода операции. С точки зрения производительности это не идеально.
def dict_fun(operator, a, b):
    return {
        'add': lambda: a + b,
        'sub': lambda: a - b,
        'mult': lambda: a * b,
        'div': lambda: a / b,
    }.get(operator, lambda: "Uncorrected")() # ()!!!!


print(dict_fun('div', 2, 10))
print(dict_fun('diasv', 2, 10))

print({True: 'да', 1: 'нет', 1.0: 'возможно'})
# ‰‰ Словари рассматривают ключи как идентичные, если результат их
# сравнения методом __eq__ говорит о том, что они эквивалентны, и если
# их хеш-значения одинаковы:
#  True == 1 == 1.0
# (hash(True), hash(1), hash(1.0)) = (1, 1, 1)
