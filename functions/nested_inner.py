def speak(text):
    def whisper(_):
        return _.lower() + 'from Inner Function'
    return whisper(text)


print(speak('Hello, '))
# print(whisper('Не существует за пределами функции speak'))
# print(speak.wisper)


def volume(value):

    def turn_up(_):
        return _.upper() + ' too quiet volume turned up'

    def turn_down(_):
        return _.lower() + ' too loud, volume turned down'
    if value > 0.5:
        return turn_up
    else:
        return turn_down


volume_level = volume(0.6)

print(volume_level('Music is'))