# generate lists with range functions
numbers = list(range(1,21))
print(numbers)

# pop method is used to empty or delete the list and someting 
# more about pop method
# pop method returns the pop item from the list to retrive lost data
poped_item = numbers.pop()
print(poped_item)

# index method in Python
# in index(value,start,stop)
# index shows the position of the value passed
print(numbers.index(4,1,10))

# pass list in a function
#  we made a funtion that make negative numbers list
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
# calling negative list function
print (negative_list(numbers))
