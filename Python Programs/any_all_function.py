# any and all functions
# all function
# if all values are true then output is true 
# and if one value is false and rest are true
# then the output is false

# any function 
# if any one value is true then output is true
#  if  all value is false then the output is false

# any and  all function use

numbers1 = [i for i in range(1,11)] 
numbers2 = [i for i in numbers1 if i % 2 == 0 ]
print(all(num%2==0 for num in numbers1))
print(all(num%2==0 for num in numbers2))
print(any(num%2==0 for num in numbers1))
print(any(num%2==0 for num in numbers2))
