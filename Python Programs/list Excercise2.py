# Making function with 
# reverse method to reverse a items of the list
# reverse method 
# does not return any thing it only make changes in list
def Reverse_list(l):
    l.reverse()
    return l

# Making a function with list slicing 
def Reverse_list(l):
    r=l[::-1]
    return r

# Maing a Same funtion 
# with pop method,append method and return method
def Reverse_list(l):
    Reverse = []
    # the loop will run until the length of the list
    for i in range(len(l)):
        # pop method always by default pop from last index  of the list
        Popped_item = l.pop()
        # append method always append at the last index of the list
        Reverse.append(Popped_item)  
    return Reverse

# Applying Function
number = list(range(1,11))
print(Reverse_list(number))