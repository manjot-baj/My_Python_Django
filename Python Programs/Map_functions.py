# Map function is iterable
# Map function takes map(your_function, argument_for_function)
numbers = [num for num in range(1,11)]
squares = list(map(lambda a: a**2,numbers))
print(squares)