# instead of [] use () rest same as list comprehension
even = lambda num : ( i for i in range(1,num+1) if i % 2 == 0 )
for i in even(10):
    print(i)
