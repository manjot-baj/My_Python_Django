# Assigning function to a variable 
# and using that variable as Function.
def Square(num):
    # Doc String
    """ Takes number and gives its Square """
    return num ** 2
# Assigning function to a variable 
s = Square
# using the variable as Function
print(s(20))
# Normal function call
print(Square(20))