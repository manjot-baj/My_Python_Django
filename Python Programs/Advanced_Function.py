# defing the function that zip multiple list
# and gives the avg 

# with normal code 

def avg_list1(*args):
    new_list=[]
    for numpairs in zip(*args):
        avg = sum(numpairs)/len(numpairs)
        new_list.append(avg)
    return new_list

# with lambda code 
avg_list = lambda * args:[ sum(numpairs)/len(numpairs) for numpairs in zip(*args)]
number1 = [i for i in range(1,11)]
number2 = [i for i in range(11,21)]
number3 = [i for i in range(21,31)]
print(avg_list(number1,number2,number3))
print(avg_list1(number1,number2,number3))