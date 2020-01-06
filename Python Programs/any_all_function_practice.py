#  practice of all and any function
def Add_total(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        Total=0
        for num in args:
            Total += num
        return Total
    else:
        return "Wrong input"

number = [i for i in range(1,11)]
number1=["1","2","2"]
print(number)
print(Add_total(*number1))
