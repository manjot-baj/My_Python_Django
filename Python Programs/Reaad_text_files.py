# open function
# opens your file to read or write 
# but you to make object of this function

# read method
# reads the contant of your file

# seek method
# to change the position of the blinking cursor

# tell method
# tells the position of the blinking cursor

# readline method
# reads single line from file 

# readlines method 
# returns contant of file in list format

# close method
# to close your file to avoid corruption of file

# closed
# to see is file is closed or not, gives boolean output

f = open("file.txt")
print(f.tell())
print(f.read())
print(f.tell())
f.seek(0)
print(f.read())
f.close()

f = open("file.txt")
print(f.readline())
print(f.readlines())
print(f.closed)
f.close()

# Note : the file that we are reading is exist in same folder
# if you want to read file from different directory
# then write the path of the file inside the open funtion 
# and to avoid escape sequence error use r 
# ex note : the following file is not exist in drive just for ex
# f = open(r"e:/somefolder/somefolder/file")

# you can read file with the help of with block
with open("file.txt") as f:
    print(f.read())
print(f.closed)
# in with block there is context manager that handles
#  all open and close system so you dont need to close
# the file 