
# excercise1 for while loop
# n=int(input("Enter the nth number to see the sum of natural numbers : "))
# i = 1
# t = 0
# while i <= n:
#     t += i
#     i += 1
# print(t)

# excercise2 for while loop
# num=input("Enter numbers : ")
# total = 0
# i = 0
# while i < len(num):
#     total += int(num[i])
#     i += 1
# print(total)

# excercise3 for while loop
name=input("Enter name : ")
i=0
temp=""
while i < len(name):
    if name[i] not in temp:
        temp += name[i]
        print(f"{name[i]}:{name.count(name[i])}")
    i += 1

