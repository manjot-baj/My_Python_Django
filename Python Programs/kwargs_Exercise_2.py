# Making a function that takes a list
# and return the strings of list in titled format 
# and if user pass one more argument with list 
# as Reversed_str=True then it reverse the strings
# of the list and also title the reversed string.
def func(User_list,**kwargs):
    # get method will get the key
    if kwargs.get("reversed_str") == True:
        # if condion for second argument
        # title method will change
        # the first index valueof string into caps
        # used list_comprehension
        return[string[::-1].title() for string in User_list]
    else:
        # else condition
        # used list_comprehension
        return [string.title() for string in User_list]

        
# Calling Function 
my_list=["manjot","singh","bajwa"]
print(func(my_list,reversed_str=True))
    