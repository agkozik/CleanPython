def integers():
    for i in range(1, 9):
        yield i


def squared(sequence):
    for i in sequence:
        yield i * i


chain = squared(integers())

print(list(chain))


def negatived(seq):
    for i in seq:
        yield -i


chain = negatived(squared(integers()))
print(list(chain))
# --------------------сокращенная форма----------------
ints = range(1, 9)
squared = (i*i for i in ints)
negatived = (-i for i in squared)
print(list(negatived))