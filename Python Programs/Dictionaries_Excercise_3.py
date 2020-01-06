# Adding and Deleting data from the Dictionary
# It is a empty dictionary
Games = {}
# Adding data in empty dictionary
Games["Name"]="Assassins Creed"
Games["Size"]="15gb"
Games["Type"]="RPG"
Games["No of Character"]=5
Games["Characters"]=["ezio","altair","connor","edward","arno"]

# Deleting data
# pop method
Poped_Item = Games.pop("No of Character")
print(Poped_Item)
# It returns the actual datatype of the poped_item
print(type(Poped_Item))
print(Games)

# popitems method
# It will pop the random element of your dictionary
Poped_Item1 = Games.popitem()
# It will return a tuple data type
print(Poped_Item1)
print(type(Poped_Item1)
print(Games)