def adder(x, y):
    return x + y


print(adder(1, 2))

adder = (lambda x, y: x + y)
print(adder(3, 4))

print((lambda x, y: x + y)(5, 6))


def adder(y):
    return lambda x: x + y


print(adder(10)(20))
# ------------------------------------------------------------
filtered_list = list(filter(lambda x: x % 2 == 0, range(16)))
print(filtered_list)


filtered_list = [x for x in range(16) if x% 2 == 0]
print(filtered_list)
# ------------------------------------------------------------

tuples = {(1, 'd'), (2, 'b'), (3, 'c')}
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)
sorted_tuples_in_range = sorted(range(-10, 10), key=lambda x: x * x)
print(sorted_tuples_in_range)

