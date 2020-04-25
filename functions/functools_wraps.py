# проблема - сокрытие метаданных:
def greet():
    """Вернуть приветствие"""
    return 'Привет!!!'


def uppercase(function):

    def wrapper():
        original_result = function()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


decorated_greet = uppercase(greet)
print('Мы видим только метаданные обертки, а не самой функции:')
print('greet.__name__: ', greet.__name__)
print('greet.__doc__ ', greet.__doc__)

print('decorated_greet.__name__ ', decorated_greet.__name__)
print('decorated_greet.__doc__ ', decorated_greet.__doc__)


print('\nА теперь Отлаживаемые декораторы:')

import functools


def uppercase(func):
    @functools.wraps(func) #  - хорошая практика для поддержки кода вешать эту анотацию, упрощает дебаг (+метаданные)
    def wrapper():
        return func().upper()
    return wrapper


@uppercase
def greet():
    """Вернуть приветствие"""
    return 'Привет!!!'


print(greet.__name__)
print(greet.__doc__)