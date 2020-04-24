from contextlib import contextmanager


@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield file
    finally:
        file.close()


with managed_file('hello.txt') as file:
    file.write('hello, ufkuu')
    file.write('!!!')




