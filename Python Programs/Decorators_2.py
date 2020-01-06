# modifying decorator
# imported in order to avoid doc string of wrapper function in your function
from functools import wraps
def Decorator_function(Function):
    # Doc String
    """ Enhances the Performance of your function """
    # Used Closure
    # using wrap decorator to avoid the doc string problem
    @wraps(Function)
    # any value can be passed in wrapper
    def Wrapper_Function(*args,**kwargs):
        """ This is Wrapper Function """
        # wrinting enhancer code
        print(f"You are Using {Function}\nThis Is Awesome Function")
        # calling the main function to enhance
        # returning also
        return Function(*args,**kwargs)
        # returns the inside function
    return Wrapper_Function

# Our function
@Decorator_function
def my_sum(num1,num2):
    # Doc String
    """This is for adding two numbers """
    return num1 + num2

print(my_sum(5,5))
print(my_sum.__doc__)