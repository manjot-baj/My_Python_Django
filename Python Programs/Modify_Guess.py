import random
for X in range (1,101):
    A=random.randint(1,101)
user_number=int(input("enter any number between 1 to 101 :"))
GameOver = False
Count = 0
while not GameOver:
    if user_number == A :
        print("yay you win")
        print(f"You took {Count} trys")
        GameOver = True
    else:
        if user_number < A:
            print("Your Number is lower than our number ... Try Again")
            Count +=1
            user_number = int(input("enter any number between 1 to 101 :"))
        else:
            print("Your Number is Higher than our number ... Try Again")
            Count += 1
            user_number = int(input("enter any number between 1 to 101 :"))


            


