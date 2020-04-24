def hello_decorator(function):
    return function


def hello():
    return 'Hello'


wrapper = hello_decorator(hello)
print(wrapper())

print('------------------ Тоже самое, но с использованием аннотаций -------------------------------------')


@hello_decorator
def wrapper():
    return 'Hello'


print(wrapper())
