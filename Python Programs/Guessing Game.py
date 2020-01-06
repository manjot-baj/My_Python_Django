# number guessing game
import random
for x in range(1):
    our_random_no=random.randint(1,100)
print( our_random_no)
print("Welcome to number guessing game.\nenter a random number between 1 to 100,\nand if your random number matches by our random number,\nthen you will win this game. ")
# print(our_random_no) #if you want to check win condition.
user_random_no=int(input("Enter a random number between 1 to 100 : "))
if user_random_no == our_random_no:
     print(f"our random number is {our_random_no} and your random number is {user_random_no}.\nyour random number Matches by our random number.\nCongratulations....you WIN THIS GAME!!! ")
elif user_random_no > our_random_no:
    print(f"our random number is {our_random_no} and your random number is {user_random_no}.\nyour random number is greater then our random number.\nsorry....you lose!!! ")
elif user_random_no < our_random_no:
    print(f"our random number is {our_random_no} and your random number is {user_random_no}.\nYour random number is less then our random number.\nsorry....you lose!!! ")
else:
    pass