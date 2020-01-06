# Making a funtion that count the sublist items in your list
def lists_in_lists(l):
    # taking variable to store the count of elements
    count=0
    # for each iem in list 
    for i in l:
        # check the condition 
        # that the datatype of that item is list or not
        if type(i) == list:
            # if the item in list is list then increase the count by 1
            count+= 1
        # return the count 
    return count

li=[1,2,3,[3,4,5],0,[1,2,3]]
print(lists_in_lists(li))