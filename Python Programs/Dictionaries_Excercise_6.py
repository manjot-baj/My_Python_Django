# Making a Function that takes 
# one argument in number  as nth number 
# and prints dictionary of cubes of nth numbers 

def cube_dict(n):
    # Made a empty dictionary
    Cubes = {}
    # for each key in dictionary till range n
    for i in range(1,n+1):
        # Makes the dictionary means add the key and values
        Cubes[i] = i**3
        # Returns the full complete dictionary with cubes of nth number
    return Cubes
# Calling our function 
print(cube_dict(10))

# Doing it by user input
user = int(input("Enter nth number to see the cubes : "))
print(cube_dict(user))

# Making a word counter funtion 
# that takes one argument as string and
# that counts the no of words repeating in you string
def word_counter(String):
    # Taking Empty Dictionary
    Count = {}
    # For ech char in String
    for char in String:
        # Add each string 
        # char=key with count=value in Count Dictionary 
        Count[char] = String.count(char)
        # Return Dictionary
    return Count
# Calling our Function
print(word_counter("Harshit"))