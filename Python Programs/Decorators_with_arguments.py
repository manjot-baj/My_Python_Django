from functools import wraps
def only_Datatype_allow(datatype):
    def decorator(Function):
        @wraps(Function)
        def wrapper(*args,**kwargs):
            if all([type(arg)== datatype for arg in args]):
                return Function(*args,**kwargs)
            return "Invalid input"
        return wrapper
    return decorator

@only_Datatype_allow(int)
def add_all(*args):
    total = 0
    for i in  args:
        total += i
    return total
print(add_all(1,2,3))
print(add_all(1,2,3,"M","A","N","J","O","T"))

@only_Datatype_allow(str)
def string_join(*args):
    string = ""
    for i in args:
        string += i
    return string

print(string_join("M","A","N","J","O","T"))
print(string_join("M","A","N","J","O","T",123))