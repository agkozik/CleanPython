# ------------------------ включение в диапазон -------------------------------------

squares = []
for x in range(10):
    squares.append(x * x)
print(squares)
# короткая форма записи:
squares = [x * x for x in range(10)]
print(squares)

# ------------------------с фильтрацией значений-------------------------------------
filtered_squares = []
for x in range(10):
    if x % 2 == 0:
        filtered_squares.append(x * x)
print(filtered_squares)

# короткая форма записи:
filtered_squares = [x * x for x in range(10)
                    if x % 2 == 0]
print(filtered_squares)

# ------------------------ включение в множество -------------------------------------
set_values = {x * x for x in range(-9, 10)}
# set(set_values)
print(set_values) # {64, 1, 0, 36, 4, 9, 16, 81, 49, 25}
# ------------------------ включение в словарь -------------------------------------
dict_values = {x: x * x for x in range(5)}
print(dict_values) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
