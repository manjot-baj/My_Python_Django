# Lists in Python
fruits=[]
fruits.append('Apple')
fruits.append('Mango')
fruits.append('Orange')
fruits.append('Melon')
User=input("Enter Your Name : ")
if User[0] == 'A' or User[0] == 'a' :
    print(f"Your Lucky Fruit is {fruits[1]}")
elif User[0] == 'M' or User[0] == 'm' :
    print(f"Your Lucky Fruit is {fruits[0]}")
else :
    print(f"Your Lucky Fruits are {fruits[2]} and {fruits[3]}")

# extend method and insert method
vegiee1=["tomato","Brinjal","pumkin"]
vegiee2=["potatoes","Onions","Ladyfinger"]
# vegiee1.extend(vegiee2)
# veg1=vegiee1 + vegiee2
# print(veg)
vegiee1.insert(2,"haldi")
print(vegiee1)
vegiee1.append(vegiee2)
print (vegiee1) #append method with list creates list under list

