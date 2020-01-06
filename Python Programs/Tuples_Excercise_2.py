# Fuctions that returns two values
# return it in tuples
# for example
def add_multiply(num1,num2):
    add = num1 + num2
    multiply= num1 * num2
    return add,multiply
# it will print it in tuple
print(add_multiply(55,60))
# to avoid the condition you can store elements in variable
# In short unpacking the tuple
add, multiply = add_multiply(55,60)
print(add)
print(multiply)

# more about tuples 
# how to create tuples with range
gargan = tuple(range(1,11))
print(gargan)

# how to convert tuple to list
# variable = list(tuple) = list
gargan1 = list(tuple(range(1,11)))
print(gargan1)
