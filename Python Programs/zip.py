# zip function is used to zip
# the values of the lists or the tuples
numbers = tuple(i for i in range(1,11))
names = ["a","b","c","d","e","f","g","h","i","j"]
names1 = ["a","b","c","d"]
name2 = ("manjot",)
ziped=list(zip(numbers,names,names1,name2))
print(ziped)

# if any list has list of two values
# or any tuple with tuple of two values then
# you can convert that tuple or list into dictionary directly
 