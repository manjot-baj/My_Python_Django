# * args is used to pass multiple arguments in function
# here insted of args you can write any parameter-variable
#  but for convention we write args.
def Add_total(*args):
    Total=0
    for num in args:
        Total += num
    return Total
# *Args return tuple datatype
def show_input_int(*args):
    return(args)

# print(Add_total(1,2,3,4,5,6,7,8,9,10))
# output : 55
# print(show_input_int(1,2,3,4,5,6,7,8,9,10))
# output :(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# * args with normal parameters
# if you pass a normal parameter with *args
#  then return of the normal parameter 
# is not included in *args 
# ex : def ex(normal_para,*args)
# return will be normal_return (*args return)
# example:
def Multiply_args(num,* args):
    Multiply = 1
    for i in args:
        Multiply *= i
        # Multiply *=num
    return Multiply

# print(Multiply_args(2,2,3))
# when   Multiply *=num is not written
# Output :6 
# when   Multiply *=num is  written
# output : 24

# you can use args as argument
# Suppose you are passing a list or tuple as a argument
# then the * args will take it as one single argument 
# and perform the function.
# but if you pass * and your list or tuple
#  then it will unpack the items for performing function 
# ex : print(my_function(* my_list/tuple))
List1 = [1,2,3]
tuple1 = (3,2,1,2)
print(Multiply_args(*List1))
print(Multiply_args(*tuple1))