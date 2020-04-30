import json

mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(json.dumps(mapping, indent=4, sort_keys=True))
#{
#     "a": 23,
#     "b": 42,
#     "c": 12648430
# }

# проблемы библиотеки json:

#print(json.dumps({all: 'yup'})) # TypeError: keys must be str, int, float, bool or None, not builtin_function_or_method

mapping['d'] = {1, 2, 3}
#print( json.dumps(mapping)) #TypeError: Object of type set is not JSON serializable