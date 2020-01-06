# list inside list ----> 2D list in Python and if there
# is list inside list inside list then it is ------> 3D List in Python
matrix=[["a","b","c"],["d","e","f"],["g","h","i"]]
#for loop tp print each elements of the list of list
for sublist in matrix:
    for li in sublist:
        print(li)