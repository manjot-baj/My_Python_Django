print("Welcome to Movie Ticket Booking App")
Movie_id1=101
Movie_id2=102
Movie_id3=103
Movie_id4=104
Movie_id5=105

Movie_Name1="The Conjuring"
Movie_Name2="The Conjuring 2"
Movie_Name3="The Conjuring 3"
Movie_Name4="The Conjuring 4"
Movie_Name5="The Conjuring 5"

Type1="Horror"
Type2="More Horror"
Type3="most Horror"
Type4="Not for you Skip it!!!"
Type5="Are You Nuts!!!"

Movie_No_1_Cost = 150
Movie_No_2_Cost = 160
Movie_No_3_Cost = 170
Movie_No_4_Cost = 180
Movie_No_5_Cost = 200

print(f"The Collection of Movies we Have \nCode\t Movie\t Type\t Cost\n{Movie_id1} {Movie_Name1} {Type1} {Movie_No_1_Cost}\n{Movie_id2} {Movie_Name2} {Type2} {Movie_No_2_Cost}\n{Movie_id3} {Movie_Name3} {Type3} {Movie_No_3_Cost}\n{Movie_id4} {Movie_Name4} {Type4} {Movie_No_4_Cost}\n{Movie_id5} {Movie_Name5} {Type5} {Movie_No_5_Cost} ")

User=int(input("Select the Movie ID to book ticket : "))
No_of_Tickets=int(input("How Tickets You Want : "))
if User == 101:
    Movie_No_1_Cost *= No_of_Tickets
    print(f"You Selected Movie\n{Movie_id1} {Movie_Name1} {Type1} {Movie_No_1_Cost}")
elif User == 102:
    Movie_No_2_Cost *= No_of_Tickets
    print(f"You Selected Movie\n{Movie_id2} {Movie_Name2} {Type2} {Movie_No_2_Cost}")
elif User == 103:
    Movie_No_3_Cost *= No_of_Tickets
    print(f"You Selected Movie\n{Movie_id3} {Movie_Name3} {Type3} {Movie_No_3_Cost}")
elif User == 104:
    Movie_No_4_Cost *= No_of_Tickets
    print(f"You Selected Movie\n{Movie_id4} {Movie_Name4} {Type4} {Movie_No_4_Cost}")
else :
    Movie_No_5_Cost *= No_of_Tickets
    print(f"You Selected Movie\n{Movie_id5} {Movie_Name5} {Type5} {Movie_No_5_Cost}")

