# using * operator with zip
names = [("Manjot",21),("Satpal",44),("Pratima",42),("Charan",14),("Dheer",12),("Family",5)]
l1,l2 = list (zip(*names))
print(l1)
print(l2)

# program to append max values form two list 
# with max and zip function
number_list = [1,2,3,4,5,6]
number_list_2 = [10,9,8,7,34,44]
number_list_3 = []
for numpair in zip(number_list,number_list_2):
    number_list_3.append(max(numpair))
print(number_list_3)
    
