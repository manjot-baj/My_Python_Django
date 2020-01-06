#  Making a function that reverse an elements from the list
def Reverse_list_elements(l):
    elements = []
    # for each element in list 
    for i in l:
        # Reverse the elements of the list
        elements.append(i[::-1])
        # return the elements
    return elements

number = ["abc","tuv","xyz"]
print(Reverse_list_elements(number))
