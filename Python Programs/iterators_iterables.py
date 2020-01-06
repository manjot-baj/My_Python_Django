# list tuples,strings these are iterables
# fuctions that return objects are iterator

# ex: iterables
# the following is a list
numbers = [i for i in range(1,11)]
# In iterables the iter function is called and 
# then next function is called
# and when the value ends the iteration stops
numbers2= iter(numbers)
print(next(numbers2))
print(next(numbers2))
print(next(numbers2))
# ex : iterators
# the following is a filter function which returns
#  object of filter function and in this function 
# it directly calls the next function no need of iter function
# and when the value ends the iteration stops
evens_1 = filter(lambda a:a%2==0,numbers)
print(next(evens_1))
print(next(evens_1))
print(next(evens_1))

