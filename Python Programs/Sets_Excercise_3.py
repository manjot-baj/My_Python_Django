# in keyword in sets and for loop

set1={1,2,3,4,5,6}
set2={1,2,3,4,5,10}
set3={9,3,1,2,5,6}

# in keyword to 
# check if the item is there is present in set or not

if 1 in set1 :
    print("present")
else:
    print("not present")

# for loop 
for item in set3:
    print(item)

for item in set2:
    print(item)

for item in set1:
    print(item)

# union
# using pipe | symbol
print(set1|set2|set3)

# intersection
# using and & symbol
print(set1&set2&set3)