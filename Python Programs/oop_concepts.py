# Encapsulation : 
# Writing or defing varaible and writing functionallity,
# of that variable and writing both of this in a same class, 
# or encapsulating the variables,functions with there 
# functionallity is called encapsulation. 

# ex:
class My_Class:
    def __init__(self,some_random_variable):
        self.some_random_variable = some_random_variable
    def some_random_variable_function(some_random_function_variable):
        my_code = "something"
        return my_code

# Abstraction:
# Using any functionallity without knowing,
# the working algorithm behind that functionallity
# ex :
list1 = ["c","a","b"]
list1.sort()
print(list1)
# output : 
# ['a', 'b', 'c']
# Now we just used the sort function to sort the list1,
# but we dont see the algorithm behind that function.

# Naming Convention
# In Python everything is public nothing is private
# but to inform other developers that you should not 
# change this particular function or variable, you can 
# use Naming convention
# ex: _yourvariable
class My_Class:
    def __init__(self,some_random_variable):
        # here _some_random_variable is private ,
        #  "just to tell other developers"
        self._some_random_variable = some_random_variable
    def some_random_variable_function(some_random_function_variable):
        my_code = "something"
        return my_code

# Name Mangling
# ex: __name__ 
# this type of convention is called dunder or magic methods
# with Name mangling python changes the name

