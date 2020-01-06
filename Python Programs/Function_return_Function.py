# In this you have function inside function and 
# it returns inside function
# It is also called as Closures and also called as
# First Class Functions
def function1():
    def function2():
        print("This is function 2 inside function 1 ")
    return function2
# if you store function 1 in variable then it 
# stores the function 2 and you have call variable 
# means function2
# logic
# if box 1 has box 2 inside it  and if you keep box 1 
# in  a box then 
# it has box2 inside it and if you call box 
# then you will get box2
var = function1()
var()