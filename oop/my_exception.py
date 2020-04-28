def validate_name(name):
    print(len(name))
    if len(name) < 3:
        raise NameLengthException(name)


class NameLengthException(ValueError):
    pass


validate_name('d')