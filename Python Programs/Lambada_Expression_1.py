# Making a function that takes a list as argument
# and reverse the string of the list and returns the reversed list
# and if another argument is passed as Capital_string = True
# then it returns the reverse string in capital. 
# Using Lambda expression,list_comprehension,
# Kwargs,functions like get(),upper(),forloop,if-else.
# get() will get the key and upper will make string in caps.
# with lambda we can def a function in one line of code
# Lambda funtions our Anonymous functions.

# ex Normal code :
def normal_reverse (list1,**kwargs):
    List1 = []
    for string in list1:
        if kwargs.get("Capital_String") == True:
            List1.append(string[::-1].upper())
        else:
            List1.append(string[::-1])
    return List1
# the above function took 8 lines of code
        
# Our fuction lambda code took 1 line
lambda_reverse = lambda list1,**kwargs : [string[::-1].upper() if kwargs.get("Capital_String") == True else string[::-1] for string in list1]

# Caling lambda_reverse function
listed = ["manjot","singh","bajwa","satpal"]
print (lambda_reverse(listed))
print (lambda_reverse(listed,Capital_String = True))

# Calling normal_reverse function
print (normal_reverse(listed))
print (normal_reverse(listed,Capital_String = True))

# output of both function will be same
