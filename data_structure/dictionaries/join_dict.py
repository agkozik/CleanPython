first_dict = {
    'a': 1,
    'b': 2,
}

sec_dict = {
    'b': 3,
    'c': 4,
}

union_dict = {}
union_dict.update(first_dict)
print(union_dict)
union_dict.update(sec_dict)
print(union_dict)
# реализация update
#def update(dict1, dict2):
     # for key, value in dict2.items():
     #     dict1[key] = value

# для слияния исключительно двух словарей
join_dict = dict(first_dict, **sec_dict)
print(join_dict)

# новый с версии 3.5 join
# получаем ту же самую стратегию разрешения конфликтов:
# правая сторона имеет приоритет, а значение в sec_dict переопределяет любое
# существующее значение под тем же самым ключом в first_dict
new_join = {**first_dict, **sec_dict}
print(new_join)                     # {'a': 1, 'b': 3, 'c': 4}
print({**sec_dict, **first_dict})   # {'b': 2, 'c': 4, 'a': 1}

