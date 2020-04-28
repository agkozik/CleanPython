def repeater(value):
    while True:
        yield value


# инструкция yield приостанавливает функцию и сохраняет ее локальное состояние
# Исполнение может # быть возобновлено в любое время вызовом функции next() с генератором в качестве аргумента
for i in repeater('hi generator'):
    print(i)