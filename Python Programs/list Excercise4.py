# Making function for filtering odd and even numbers in list
def Filter_odd_even(l):
    # Taking two empty list
    odd_nums = []
    even_nums = []
    # for each elemnts of the list
    for i in l:
        # checking even condition
        if i % 2 == 0:
             # makes list of even elements
            even_nums.append(i)
            # checking odd condition
        else:
            # makes list of odd elements
            odd_nums.append(i)
        # puting both the list in one list
    output = [odd_nums,even_nums]
    # returning the final list
    return output

number = list(range(1,11))
print(Filter_odd_even(number))