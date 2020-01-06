# Exercise
# defing a decorator that tells
#  the run time timing of the funtion 
# importing time
import time
from functools import wraps
# defing our decorator
def Calculate_time(Function):
    """ Calculates the run time of your function """
    # using wrap decorator to avoid the doc string problem
    @wraps(Function)
    def Wrapper_Function(*args,**kwargs):
        # code that will tell the timing
        t1 = time.time()
        return_value = Function(*args,**kwargs)
        t2 = time.time()
        t3 = t2 - t1
        print(f"The Function {Function.__name__} took {t3} secs to run")
        # returning function
        return  return_value
    return Wrapper_Function
# calling decorator
@Calculate_time
def my_sum(num1,num2):
    # Doc String
    """This is for adding two numbers """
    return num1 + num2
print(my_sum(5,5))

@Calculate_time
def Square(n):
    return [i**2 for i in range(1,n+1)]
print(Square(10))