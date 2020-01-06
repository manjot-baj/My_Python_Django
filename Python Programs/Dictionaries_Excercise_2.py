# in keyword and iterations in dictionary 

# It is a empty dictionary
Games = {}
# adding values in empty dictionary
Games["Name"]="Assassins Creed"
Games["Size"]="15gb"
Games["Type"]="RPG"
Games["No of Character"]=5
Games["Characters"]=["ezio","altair","connor","edward","arno"]

# check if key exist in dictionary
if "Name" in Games:
    print("present")
else:
    print("not present")

# check if value exist in dictionary---->value method
if ["ezio","altair","connor","edward","arno"] in Games.values():
    print("present")
else:
    print("not present")

# loops in dictionary
# the following loop will print the keys present in dictionary
for i in Games:
    print(i)
# to print values
for i in Games.values():
    print(i)

# you can also do this to print values of dictionary
for i in Games:
    print(Games[i])

# value method 
cyber = Games.values()
print(cyber)
# returns values in dict_values datatype
print(type(cyber))

# key method
cyber = Games.keys()
print(cyber)
# returns keys in dict_keys datatype 
print(type(cyber))

# items method
# It is the most used method
# It returns items in dict_items datatype
# It has a list of tuples
# ex : dict_items([(),(),()])
Games_items = Games.items()
print(Games_items)
print(type(Games_items))

# looping with items method in dictionary
for keys,values in Games.items():
    print(f"The key is {keys} and the Value is {values}")

# looping with items method in dictionary
for i in Games.items():
    print(f"{i}......{len(i)}")