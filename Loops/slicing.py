# шаблон [начало:конец:шаг]:
# Чтобы избежать ошибок смещения на единицу, важно помнить,
# что верхняя граница всегда не учитывается
my_list = [1, 2, 3, 4, 5]
print(my_list[1:3:1])  # [2, 3]

print(my_list[1:3])  # если не указан step то он равен 1

print(my_list[::2])  # [1, 3, 5] каждый второй элемент
print(my_list[::-1])  # [5, 4, 3, 2, 1] в обратном порядке

my_str = 'abcde'
print(my_str[::-1])  # edcba
revers_str = ''.join(reversed(my_str))
print(revers_str)

# очистка списка:
del my_list[:]
print(my_list)  # []
# или:
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)

# замена всех элементов листа без уничтожения списка, т.е сохранились ссылки
lst = [1, 2, 3]
origin_lst = lst
lst[:] = [7, 8, 9]
print(lst) # [7, 8, 9]
print(origin_lst) # [7, 8, 9]
print(origin_lst is lst) # True

# создание мелкой копии
copied_lst = lst[:]
print(copied_lst)
print(copied_lst is lst)

# Если необходимо продублировать абсолютно все, включая и элементы, то
# необходимо создать глубокую копию списка. Для этой цели пригодится
# встроенный модуль Python copy.