# Making a generator function
import time 
# generator function
def generator_function(num):
    for i in range(1,num+1):
        yield i
# list
list1 = [i for i in range(1,101)]
t1 = time.time()
for num in list1:
    print(num)
t2 = time.time()
t3 = t2 - t1 
print(f"this is list took {t3} secs")
# takes 0.06 secs

# generator
t4 = time.time()
for num in generator_function(100):
    print(num)
t5 = time.time()
t6 = t5-t4
print(f"this is Generator took {t6} secs")
# takes 0.03 secs

# generators are fast compared to list