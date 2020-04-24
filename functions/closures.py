def volume(text, value):

    def turn_up():
        return text.upper() + ' too quite. Volume Up to ' + str(value + 0.1)

    def turn_down():
        return text.lower() + ' too loud. Volume down to ' + str(value - 0.1)
    if value > 0.5:
        return turn_down
    else:
        return turn_up


print(volume('Music is', 0.7) () )

# фабрика
def sum(number):
    # функция-сумматор
    def add(x):
        return x + number
    return add


plus_3 = sum(3)
print(plus_3(4)) # 7

print(sum(3)(5)) # 8

