

def uppercase(function):
    def wrapper():
        original_result = function()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def wrapper():
    return 'hello'


print(wrapper())

