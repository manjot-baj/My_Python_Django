# Update the dictionary

# Dictionary 1
userinfo = {
    "Name" : "Manjot",
    "age" : 21,
    "list": ["hello",34,15,["world",45,51]]
}

# Dictionary 2
# It is a empty dictionary
Games = {}
# Adding data in empty dictionary
Games["GName"]="Assassins Creed"
Games["Size"]="15gb"
Games["Type"]="RPG"
Games["No of Character"]=5
Games["Characters"]=["ezio","altair","connor","edward","arno"]

# Updating
# Update method
#  Dictionary1.update(Dictionary2)
# If the key in Dictionary1 
# is same as it is present in Dictionary2
#  then the key value of Dictionary2 
# overrides the value of Dictionary1
# In short it updates the key value

userinfo.update(Games)
print(userinfo)