phonebook = {
    'bob': 123,
    'elise': 456,
    'jon': 789,
}
print(phonebook)
print(phonebook['jon'])
phonebook['bill'] = 987
print(phonebook)
phonebook['jon'] = 987
print(phonebook)
phonebook[''] = 987
print(phonebook)
print(phonebook.keys())
print(phonebook.values())
print(phonebook.items())
squares = {i: i * i for i in range(6)}
list1 = list(range(6))
print(list1)
print(squares)
