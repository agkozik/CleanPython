from types import MappingProxyType

writable = {'один': 1, 'два': 2}  # доступный для обновления
read_only = MappingProxyType(writable)

print(read_only['один']) # 1
# read_only['один'] = 23 # TypeError: 'mappingproxy' object does not support item assignment

writable['один'] = 42
print(read_only) # {'один': 42, 'два': 2}