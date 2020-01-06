# Making generator function
# generator function
import time


def even_generator(num):
    for i in range(1, num + 1):
        if i % 2 == 0:
            yield i


# list function
def even_function(num):
    list1 = []
    for i in range(1, num + 1):
        if i % 2 == 0:
            list1.append(i)
    return list1


t1 = time.time()
for num in even_generator(10):
    print(num)
t2 = time.time()
t3 = t2 - t1
print(f"generator function took {t3} secs")
# takes 0.0009 secs

t4 = time.time()
for num in even_function(10):
    print(num)
t5 = time.time()
t6 = t5 - t4
print(f"normal function took {t6} secs")
# takes 0.0019 secs
# generator functions are fast compared to list function.
