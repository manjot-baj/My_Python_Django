# Making a function that 
# returns square of the values of the list
def square_list(l):
    Square = []
    for i in l:
        # the operator will square the value of the list (i**2)
        Square.append(i**2)
    return Square

number = list(range(1,11))
print(square_list(number))