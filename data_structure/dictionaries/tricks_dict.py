names_user_id = {
    123: 'John',
    456: 'Bill',
    789: 'Den',
}


def greeting(user_id):
    if user_id in names_user_id:
        return f'Hello, {names_user_id[user_id]}'
    else:
        return 'Hello, everyone!'


print(greeting(123))  # Hello, John
print(greeting(111))  # KeyError: 111


def greeting(user_id):
    try:
        return f'Hello, {names_user_id[user_id]}'
    except KeyError:
        return 'Hello, everyone!'


print(greeting(123))  # Hello, John
print(greeting(111))  # KeyError: 111


# В словаре Python есть метод get(), поддерживающий параметр «по умолчанию»,
# который можно использовать в качестве запасного значения
def greeting_with_def(user_id):
    return f'Hello, {names_user_id.get(user_id, "there!")}'

print(greeting_with_def(456))
print(greeting_with_def(444))

