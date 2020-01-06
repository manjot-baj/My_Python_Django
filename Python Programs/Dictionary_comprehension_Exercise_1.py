# Dictionary comprehension is used to add value 
# and make dictionary in less no of code
# make sure you keep in mind about key:value pair
#ex : Dictionary = {Key:Value loop condition} 
Square = {num:num**2 for num in range(1,11)}
print(Square)
# output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# Modifying 
Square1 = {f"Square of {num} is ":num**2 for num in range(1,11)}
print(Square1)
# output : {'Square of 1 is ': 1, 'Square of 2 is ': 4, 'Square of 3 is ': 9, 'Square of 4 is ': 16, 'Square of 5 is ': 25, 'Square of 6 is ': 36, 'Square of 7 is ': 49, 'Square of 8 is ': 64, 'Square of 9 is ': 81, 'Square of 10 is ': 100}

# Printing one by one
for Key,Value in Square1.items():
    print(f"{Key} : {Value}")
# output : 
# Square of 1 is  : 1
# Square of 2 is  : 4
# Square of 3 is  : 9
# Square of 4 is  : 16
# Square of 5 is  : 25
# Square of 6 is  : 36
# Square of 7 is  : 49
# Square of 8 is  : 64
# Square of 9 is  : 81
# Square of 10 is  : 100

# String word counter
String = "Manjot Singh Bajwa"
WordCounter = {char:String.count(char) for char in String}
print(WordCounter)
# Output : {'M': 1, 'a': 3, 'n': 2, 'j': 2, 'o': 1, 't': 1, ' ': 2, 'S': 1, 'i': 1, 'g': 1, 'h': 1, 'B': 1, 'w': 1}
