from collections import ChainMap
dict1 = {'one': 1, 'two':2, 'three': 3}
dict2 = {'four': 4, 'five': 5, 'six': 6}
chain = ChainMap(dict1, dict2)
print(chain) #ChainMap({'one': 1, 'two': 2, 'three': 3}, {'four': 4, 'five': 5, 'six': 6})
print(chain['six']) # 6
print(chain['seven']) # KeyError: 'seven'
