for x in ('Hello' for i in range(3)):
    print(x)

z = sum((x*2 for x in range(10)))
print(z)