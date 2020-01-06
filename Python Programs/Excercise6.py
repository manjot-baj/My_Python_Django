# modified version of number guessing game
import random
win_no=random.randint(1,100)
guess=1
Game_Over=False
user_no=int(input("Guess a number between 1 to 100 : "))
while not Game_Over:
    if user_no == win_no :
        print(f"you win , this game in {guess} try")
        Game_Over=True
    else :
        if user_no < win_no :
            print("too low try again")
            user_no=int(input("Guess again : "))
            guess += 1
        else :
            if user_no > win_no  :
                 print("too high try again")
                 user_no=int(input("Guess again : "))
                 guess += 1