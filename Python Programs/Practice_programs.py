# Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

def my_function():
    num = int(input('Enter any no : '))
    if num % 3 == 0 and num % 5 == 0:
        return print('FIZZ BUZZ')
    elif num % 5 == 0:
        return print('BUZZ')
    elif num % 3 == 0:
        return print('FIZZ')
    return print(num)


def my_finder():
    num1, num2 = input('Enter two numbers :').split()
    if int(num1) > int(num2):
        return print(num1)
    return print(num2)


my_function()
my_finder()
