from struct import Struct


MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.0)
# получается двоичный объект данных (blob):
print(data) # b'\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00(B'

# BLOB-объекты можно снова распаковать:
print(MyStruct.unpack(data))
