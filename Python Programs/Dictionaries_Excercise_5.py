# fromkeys method in Dictionary
# It is used to create a dictionary with same values to many keys
# ex : user = dict.fromkeys([keys],value)
user = dict.fromkeys(["Name","Age"],"Unknown")
print(user)

# Get method
# This method is used to access the key of dictionary
# It do not throw error if the key is not exist
#  in dictionary else it returns "None"

print (user.get("Name"))
# else
# key:"names" is not exist in Dictionarys
print(user.get("names"))
# It returns "None" and not throws error
# if you want to return some other text other none then
# ex : dictionary.get("key","your_text")
print (user.get("names","not present"))

# clear method is used to clear your dictionary
user.clear()
print(user)

# copy method is used to copy the data of dictionary
# ex : dictionary1 = dictionary2.copy()
# It creates a another copy of the dictionary
dictionary1 = user.copy()
print(dictionary1)

# Note : Suppose in Dictionary two keys are same then 
# the latest key value will override the previous value
# ex : Dictionary{"Key1":"Value1","Key2":"Value2","Key2":"Value3"}
# In above the last key2 value will 
# override the second last key2 value
# so "key2" : "Value3"