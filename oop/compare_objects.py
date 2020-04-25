a = [1, 2, 3]
b = a

print(a == b)
print(a is b)

c = list(a)
print(c) # [1, 2, 3]
print(c == a) #True сравнение по содержимому
print(a is c) #False сравнение по ссылке