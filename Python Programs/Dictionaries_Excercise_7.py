# Making a program that takes the input from the user
#  and stores it in Dictionary 
# and prints the user input values

# Making a empty Dictionary
User_Info = {}
# Taking input from user 
Name = input("Enter Your Name : ")
Age = int(input("Enter Your Age : "))
# Note : If the input is passed in a single variable 
# through split method then it creates list 
Fav_Movies =input("Enter Your Favourate movies : ").split(",")
Fav_Songs = input("Enter Your Favourate Songs : ").split(",")

# Adding User Values in Dictionary
User_Info["Name"] = Name
User_Info["Age"] = Age
User_Info["Fav_Movies"] = Fav_Movies
User_Info["Fav_Songs" ]= Fav_Songs

# For printing values one by one
for key,value in User_Info.items():
    print(f"{key}:{value}")
