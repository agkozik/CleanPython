vowels = {'a', 'e', 'i', 'o', 'u'}
squares = {x * x for x in range(10)}
print(vowels) #{'u', 'a', 'e', 'i', 'o'}
print(squares) #{0, 1, 64, 4, 36, 9, 16, 49, 81, 25} - неупорядоченные квадраты чисел

letters = set('alica')
print(letters.intersection(vowels))
vowels.add('x')
print(vowels)
vowels.add('x')
print(vowels)
print(len(vowels))
vowels.update('strq')
print(vowels)