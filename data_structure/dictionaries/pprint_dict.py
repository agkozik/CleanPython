import pprint


mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
mapping['d'] = {1, 2, 3}
pprint.pprint(mapping)
