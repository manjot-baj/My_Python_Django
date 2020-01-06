# defining funtion with two parameters for greater number
# def greater_num(num1,num2):
#     if num1 > num2 :
#         return num1 
#     return num2

# uno1,uno2=map(str,input("Enter two numbers : ").split(","))
# uno1=int(uno1)
# uno2=int(uno2)
# result=greater_num(uno1,uno2)
# print(f"The Greater number is {result}")

# defining funtion with three parameters for greatest number
def greater_num(num1,num2,num3):
    if num1 > num2 and num1 > num3 :
        return num1 
    elif num2 > num1 and num2 > num3:
        return num2
    return num3

uno1,uno2,uno3=map(str,input("Enter three numbers : ").split(","))
uno1=int(uno1)
uno2=int(uno2)
uno3=int(uno3)
result=greater_num(uno1,uno2,uno3)
print(f"The Greater number is {result}")
