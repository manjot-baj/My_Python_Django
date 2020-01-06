# Making a function that
#  shows the common items from the two given list
def lists_common_elements(l1,l2):
    # Logic
    # for each item in list 1 
    # if item of list 1 is present in list 2
    # then append that item in output list
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
        # return the output list with common items
    return output

# Passing numbers
n1=["1","2","3","4"]
n2=["1","2","5","6"]

# Passing words
user1 = ["sugar","pumkin","chocolate","candy"]
user2 = ["sugar","candy","beer","chicken"]

# Calling our function
print(lists_common_elements(user1,user2))