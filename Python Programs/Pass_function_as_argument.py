# Passing a function as argument in a function defined by us.
def my_map_func(Function,L):
    # Doc String
    """ Takes any Function as argument and the argument to pass in that function
    and returns the list """
    # List Comprehension
    return [Function(item) for item in L]
# Storing a function in variable and then calling that function
m = my_map_func
# List Comprehension
List1 = [i for i in range(1,11)]
# Calling our function
print(m(lambda a:a**2,List1))