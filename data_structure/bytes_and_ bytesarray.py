# bytes - неизменяемые масиивы одиночных байтов
byteS = bytes((0, 1, 2, 3))
print(byteS)
print(byteS[1])
#print(bytes((0, 256))) #ValueError: bytes must be in range(0, 256)

# bytearr - изменяемые масиивы одиночных байтов

bytesarr = bytearray((0, 1, 2, 3))
print(bytesarr)
print(bytesarr[1])
print(bytesarr)

bytesarr[2] = 7
print(bytesarr)
del bytesarr[0]
print(bytesarr)
# Bytearrays может быть преобразован в байтовые объекты:
print(bytes(bytesarr))
