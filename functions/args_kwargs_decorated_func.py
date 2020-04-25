def trace(func):
    def wrapper(*args, **kwargs):
        print(f'Трассировка: вызвана функцией {func.__name__}() c args:{args}, kwargs:{kwargs}')

        original_result = func(*args, **kwargs)
        print(original_result)

        print(f'Трассировка: {func.__name__}() вернула: {original_result!r}')
        return original_result
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


print(say('Sasha', 'Какой-то текст'))
