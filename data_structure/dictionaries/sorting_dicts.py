# получить сортированный список пар ключ-значение в этом словаре,
# вы можете применить метод items() словаря и затем отсортировать
# результирующую последовательность на втором обходе:

xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1, 'e': -4, }
items_sort = xs.items()
print(sorted(items_sort), 'items_sort')  # [('a', 4), ('b', 3), ('c', 2), ('d', 1), ('e', -4)]

values_only_sort = xs.values()
print(sorted(values_only_sort), 'values_only_sort ')  # [-4, 1, 2, 3, 4]

values_sort = sorted(xs.items(), key=lambda x: x[0]) # [0] Это по ключу, [1] по значению
print(values_sort, 'values_sort')  # [('e', -4), ('d', 1), ('c', 2), ('b', 3), ('a', 4)]

abs_sort = sorted(xs.items(), key=lambda x: abs(x[1]))
print(abs_sort, 'abs_sort') # [('d', 1), ('c', 2), ('b', 3), ('a', 4), ('e', -4)]

reversed_sort = sorted(xs.items(), key=lambda x: x[0], reverse=True)
print(reversed_sort, 'reversed_sort [0]') # [('e', -4), ('d', 1), ('c', 2), ('b', 3), ('a', 4)]

reversed_sort = sorted(xs.items(), key=lambda x: x[1], reverse=True)
print(reversed_sort, 'reversed_sort [1]') # [('a', 4), ('b', 3), ('c', 2), ('d', 1), ('e', -4)]
# аналогично operator.itemgetter и operator.attrgetter.
import operator

result_itemgetter = sorted(xs.items(), key=operator.itemgetter(1))
print(result_itemgetter, 'result_itemgetter') # [('e', -4), ('d', 1), ('c', 2), ('b', 3), ('a', 4)]
