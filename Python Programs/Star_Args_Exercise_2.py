def Request_power_list(num,* args):
    if args:
        return[value**num for value in args]
    else:
        return "You didn't pass any args"
list1 = [i for i in range(1,11)]
print(Request_power_list(2,*list1))