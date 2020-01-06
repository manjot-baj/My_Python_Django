# Making a function that takes list and
#  returns a list with reverse strings 
def reverse_list(l):
    # List Comprehension
    # Reverse=[append condition    iteration of taken list values]
    return [i[::-1] for i in l]
# Calling our function
Names=["Manjot","Singh","Bajwa"]
print(reverse_list(Names))

# if Statement and loop with list comprehension
# After loop you write the if statement
even_nums = [i for i in range(1,11) if i%2 == 0]
odd_nums = [i for i in range(1,11) if i%2 != 0]
print(f"even : {even_nums} \n odd : {odd_nums}")