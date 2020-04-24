def echo(some_text):
    return str(some_text).upper() + '!'


print(echo('привет'))

bark = echo

print(bark('гав'))

print(bark.__name__)
print(bark.__qualname__)
print(echo.__name__)
print(echo.__qualname__)

list_of_functions = [echo, bark, str.lower, str.upper, str.capitalize]
print(list_of_functions)

for _ in list_of_functions:
    print(_, _('приветики'))

print('----------------------------------------------------------')


def greet(func):
    greet2 = func('Привет! Я функция greet2')
    print(greet2)


greet(bark)

# Функция map обходит весь список и применила функцию bark к кадому элементу списка, а list сформировал новый список:
my_uppercase_list = list(map(bark, ['я', 'учу', 'питон']))
print(my_uppercase_list)