# Decorator function is used to enhance
# the Performance of your function 
# ex : 
# This is our Function 1
def function_1():
    print("This Is Function 1")
# This is our Function 2
def function_2():
    print("This Is Function 2")
# This is our Decorator Function
def Decorator_function(Function):
    # Doc String
    """ Enhances the Performance of your function """
    # Used Closure
    def Wrapper_Function():
        # wrinting enhancer code
        print("This Is Awesome Function")
        # calling the main function to enhance
        Function()
        # returns the inside function
    return Wrapper_Function
# calling decorator
Var = Decorator_function(function_1)
# it has wrapper function inside it.
Var()

# else

function_1 =  Decorator_function(function_1)
function_1()
function_2 =  Decorator_function(function_2)
function_2()

# else

# Syntatic Sugar
# call decorator before defing your function
# @decorator and
# your function

# This is our Function 3
# Using Syntatic Sugar
@Decorator_function
def function_3():
    print("This Is Function 3")
    # calling Function
function_3()
# This is our Function 4
# Using Syntatic Sugar
@Decorator_function
def function_4():
    print("This Is Function 4")
      # calling Function
function_4()
