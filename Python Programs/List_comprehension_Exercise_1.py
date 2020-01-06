# List comprehension is used to 
# write code for list related program in less no of lines
# In Normal code
Square=[]
# Iterarate i till range(given)
for i in range(1,11):#----> Code 1
# And append (condition or Value) in each iteration
    Square.append(i**2)#----> Code 2
print(Square)
# With List Comprehension
# Square=[Code2 Code1]
# First Write what to append with condition 
# and then iteration condition
Square=[i**2 for i in range(1,11)]
print(Square)

# Similarly
Negative=[-i for i in range(1,11)]
print(Negative)

# Similarly
Names=["Manjot","Singh","Bajwa"]
Names1=[i[0] for i in Names]
print(Names1)

