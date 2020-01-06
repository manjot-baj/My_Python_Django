# Sets in Python 
# It is a unordered collection of unique items
# It has datatype as sets
h={1,2,3,4,5,61,1,2,3,4,5,61,53}
# Removes or combine the duplicate data into one 
# and returns the unique data
print(h)
print(type(h))

# to add iteems in set use add method
h.add("Manjot")
h.add(90)
h.add(69)
print(h)

# to remove some items you can use remove method
h.remove(53)
h.remove(61)
print(h)
# if you put a items in remove method
#  which is not present in set then it give key error

# Discard method 
# This method also remove or delete the data from the set
#  but if you put a item which is not present in set 
# then it does not show any error 
# as well as it does not remove anything from sets
h.discard("Singh")
h.discard(1)
print(h)

# copy method
h1=h.copy()
print(h1)

# Clear method 
h.clear()
print(h)

# Note : you cant store dictionary,list,tuples in set
# You can store any datatype rather then above ones
