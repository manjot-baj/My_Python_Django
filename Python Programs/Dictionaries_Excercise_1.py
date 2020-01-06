# dictionaries in python
#  are used because list and tuple 
# are not enough to represent the data in real time

# about dictionaries
# dictionary can store any data
# dictionary are unordered collection of data in
# key:value pair.

# example of dictionaries
user={"name":"Manjot","age":21}
print(type(user))
print(user)

# second method to create dictionaries 
user1 = dict(name="Manjot",age=21,height=5.11)
print(type(user1))
print(user1)

# In dictionaries you cannot use indexing, slicing directly
# you have to access the key
print(user1["name"])

# another way to create a dictionary of multiple data
userinfo = {
    "Name" : "Manjot",
    "age" : 21,
    "list": ["hello",34,15,["world",45,51]]
}
print(userinfo)
# creating multiple dictionaries in dictionary
userinfo1 = {

   "userno1" : { 
       "Name" : "Manjot",
        "age" : 21,
        "list": ["hello",34,15,["world",45,51]]
        } ,

    "userno2" : {
       "Name" : "RAHUL",
        "age" : 24,
        "list": ["hockey",34,15,["cool",45,51]]
        } ,
    "userno3" : {
     "Name" : "vijay",
     "age" : 20,
     "list": ["football",34,15,["creep",45,51]]
     }
}
print(userinfo1)

# Adding  values in dictionaries
# It is a empty dictionary
Games = {}
# adding values in empty dictionary
Games["Name"]="Assassins Creed"
Games["Size"]="15gb"
Games["Type"]="RPG"
Games["No of Character"]=5
Games["Characters"]=["ezio","altair","connor","edward","arno"]
print(Games)
