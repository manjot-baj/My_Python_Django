# enumerate functions our used in for loop to find 
# the position of the given list items or letters of string
# enumerate(your_input)
# for normal code 
def position(l):
    pos=0
    for string in l:
        print(f"{string}--->{pos}")
        pos += 1
names = ["Manjot","abcd","Singh","dcba"]
position(names)

# with enumerate fuction
# Defing a function that take two argument 
# takes list and a target string 
# and will return the position of target string in the list 
def position_finder(l,target):
    for pos,string in enumerate(l):
        if  string == target:
            return pos
        else:
            return -1

print (position_finder(names,"Manjot"))
print (position_finder(names,"Man"))