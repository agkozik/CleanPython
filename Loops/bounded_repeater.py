class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        else:
            self.count += 1
            return self.value


bounded_repeater = BoundedRepeater('Hello', 3)
for i in bounded_repeater:
    print(i)

