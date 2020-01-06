# Modified version of decorator 5 file used list comprehension
from functools import wraps
def only_int_allow(Function):
    def wrapper(*args,**kwargs):
        if all([type(arg)==int for arg in args]):
            return Function(*args,**kwargs)
        return "Invalid input"
    return wrapper
    
@only_int_allow
def add_all(*args):
    total = 0
    for i in  args:
        total += i
    return total
print(add_all(1,2,3))