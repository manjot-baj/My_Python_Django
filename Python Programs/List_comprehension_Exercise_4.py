# nested List with list comprehension
# ex: ex=[[1,2,3],[1,2,3],[1,2,3]]
nested_list = [[i for i in range(1,4)] for j in range(3)]
print(nested_list)