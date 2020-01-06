# Making a function that 
# takes input as one argument as list
#  and return a list with all int and float 
# types values of given list
def make_List(l):
    # In normal code 
    Sorted_List=[]
    for i in l:
        if type(i) == int or type(i) == float:
            Sorted_List.append(str(i))
    return Sorted_List
# in list comprehension
    return[str(i) for i in l if type(i) == int or type(i) == float ]

# Caling our function
list11=["hello","world",1,3,4,5.0,4.0]
# print(make_List(list11))

# Making a function that takes one argument as list
# and returns list with negative and squares
# negative when the int value is odd 
# Squares when the int value is even

# created list by list Comprehension
List1 = [i for i in range(1,11)]

# normal code
def neg_square(l):
    List2 = []
    for i in l:
        if i % 2 == 0:
            List2.append(i**2)
        else:
            List2.append(-i)
    return List2

# List comprehension
def neg_square_1 (l):
    return [i**2 if i % 2 == 0 else -i for i in l]
# Calling function
print(neg_square_1(List1))