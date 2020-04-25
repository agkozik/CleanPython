def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


print_vector(1, 2, 3) #<1, 2, 3>

tuple_vector = (1, 2, 3)
list_vector = (1, 2, 3)
dict_vector = {'x': 1, 'z': 3, 'y': 2}
print_vector(*tuple_vector) #<1, 2, 3>
print_vector(*list_vector) #<1, 2, 3>

print_vector(*dict_vector) #<x, z, y>
print_vector(**dict_vector) #<1, 2, 3>
