# Класс frozenset реализует неизменяемую версию множества set. (никаких вставок или удале-
# ний)

numbers = frozenset({1, 2, 3, 4, 5, 5, 7})
print(numbers)
#numbers.add('6') # AttributeError: 'frozenset' object has no attribute 'add'

# Множества frozenset хешируемы и могут
# использоваться в качестве ключей словаря:
dict = {frozenset({1, 2, 3}): 'hello'}
print(dict) # {frozenset({1, 2, 3}): 'hello'}