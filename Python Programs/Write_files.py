w,a,r+
with open("file2.txt","w") as f:
    f.write("hello this is file 1\n")

with open("file1.txt","a") as f:
    f.write("hello this is file 1\n")

with open("user.txt","r+") as f:
    f.write("hello this is file 1\n")
    f.seek(0)
    print(f.read())

# w
# this is write function
# it creates a file if the file is not exist and if exist it overrides
# always use this function for empty file

# a
# this is append function
# appends content at the end of the content of the file

# r+
# this is read write method
# this is used for writing and read the file 
# this function does not create file if not exist
# this function overide equal to length of the new content

# Suppose you want to read a data from a file 
# and you want to write that particular data into 
# new file then you can do it in following way
 
with open("file2.txt","r") as rf:
    with open("file3.txt","w") as wf:
        wf.write(rf.read())