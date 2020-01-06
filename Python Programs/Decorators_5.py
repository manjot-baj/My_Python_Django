from functools import wraps


def only_int_allow(Function):
    def wrapper(*args, **kwargs):
        Data_types = []
        for arg in args:
            Data_types.append(type(arg) == int)
        if all(Data_types):
            return Function(*args, **kwargs)
        else:
            return "Invalid input"

    return wrapper


@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total


list1 = [i for i in range(1, 11)]
print(add_all(1, 2, 3))
