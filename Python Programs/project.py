import random
for X in range (1,101):
    A=random.randint(1,101)
print(A)

user_number=int(input("enter any number between 1 to 101 :"))

if user_number == A :
    print("yay you win")
else :
    if user_number < A:
        print(f"Your Number is lower than our number...So,you lose, your numer is{user_number} and our random is {A}")
    else:
        print(f"Your Number is higher than our number...So,you lose, your numer is{user_number} and our random is {A}")

    # print(f"you lose, your numer is{user_number} and our random is {A}")
