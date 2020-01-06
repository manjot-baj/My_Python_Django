# filterfunction are used to filter your list or tuple
# according to your defined function
# filter function is iterable but only one time
# ex : filter(defined function,list/tuples)
# our list
numbers = [i for i in range(1,11)]
# defing function with normal code.
def is_even(num):
    return num % 2 == 0
evens =list(filter(is_even,numbers))
print(evens)
# doing iteration
for i in evens:
    print(i)
# defing with lambda expression
evens_1 = tuple(filter(lambda a:a%2==0,numbers))
print(evens_1)
# doing iteration
for i in evens_1:
    print(i)


