# Tuples in Python 
# have parenthesis and commos
# tuple are immutable
# tuple cant be updated
# with tuples you cant use methods like
# pop(),insert(),append(),etc
# in tuple you can use count(),slicing(),index(),and len()
# Example of Tuple
mixed=(1,2,3,4,5,6,7,8,9,10)
print(type(mixed))

# creating tuple with one element
# Note: if you are creating tuple with one element then
# make sure you add comma after the element 
# else python will not consider it as tuple 
# and will take  default datatype of the element
number=(1,)
print(type(number))

# loops in tuples
# can use for loop nd as well aswhile loop
for i in mixed:
    print(i)

# tuples without parenthesis 
# Python by default takes it as tuple
# if return in below format
dancers = "micheal","jordon","lily","casper"
print(type(dancers))

# Tuples unpacking 
# elements of the tuples
#  can be assign to variables in order to unpack
# Note: one variable can take one element only 
# and while unpacking you have to assign
#  no of variables = no of elements in tuple
dancers = "micheal","jordon","lily","casper"
a,b,c,d=dancers
print(c)

# List in Tuples
chewgum = ("freshgum","saltgum",["boomer","centerfresh","chewchew","chupachups"])
# count() in tuples
print(chewgum.count("freshgum"))
# len() in tuples
print(len(chewgum))
# slicing in tuples
print(chewgum[2])

# List in Tuples can be mutable
# using pop for list in tuple
chewgum[2].pop()
# using append to update list in tuple
chewgum[2].append("centerfruit")
print(chewgum)

# In list and in tuple you can use max and min method
num1=23,25,2,1
print(max(num1))
print(min(num1))
# there is one more method 
# you can use which is sum
#  to sum all the values of the tuples
print(sum(num1))