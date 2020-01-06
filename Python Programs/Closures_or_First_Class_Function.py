# Here is the ex of closure
# Defing a function to power that takes 
# argument as any no as power. 
def to_power(x):
    # Doc String
    """Takes power and Assign that power 
    to a number function for the further  
    functionalty n**Userinput=ans """
    # Defing another function inside function 
    # that takes no as argument
    #  and returns the power of the number.
    def number(n):
        """ Take Number and returns the power of the given 
        number ex : Userinput**to_power(Userinput)=ans """
        return n**x
    return number

Cube = to_power(3)
print(Cube(2)) 