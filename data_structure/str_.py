string1 = 'abc'
print(string1[1])
# string1[1] = 'B' # нельзя изменить str: TypeError: 'str' object does not support item assignment
list_string1 = list(string1)
print(list_string1)
print(' разделитель '.join(list('abcd')))
print(string1)
list_string1.append('E')
print(list_string1)
print('-'.join(list_string1))
print(type(string1))
print(type(string1[1]))