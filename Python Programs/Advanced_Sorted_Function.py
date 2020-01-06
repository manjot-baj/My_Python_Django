# Sorted function
List1 = ["Zaid","Xylo","Anand","Bismil"]
tuple1 = ("Zara","Kaira","Sara","Tara")
set1 = {"Undon","Gandon","Pandon","Sandon"}
# for list
List2 = sorted(List1)
# print(List2)
# for tuple
tuple2 = sorted(tuple1)
# print(tuple2)
# for set
set2 = sorted(set1)
# print(set2)
# sorted function does not change the original list/tuple/set
# but takes it and return in list datatype 
# and you can store it in different variable

# Advanced Sorted
Games = [
    {"Game_Name":"Assassins Creed Odessey","Price":7000},
    {"Game_Name":"Grand Theft Auto:V","Price":2500},
    {"Game_Name":"Counter Strike Global Offensive","Price":1500},
    {"Game_Name":"PUBG","Price":5500}
]

Sorted_Games = sorted(Games,key = lambda dic:dic["Price"],reverse = True)
Max_Games = max(Games,key = lambda dic:dic["Price"])["Game_Name"]
Min_Games = min(Games,key = lambda dic:dic["Price"])["Game_Name"]
print(Sorted_Games)
print(f"{Max_Games} has the highest price among other games ")
print(f"{Min_Games} has the Lowest price among other games ")