# in exception handling we use
# try except else finally clause 
# # here we use try and except
# inside try write the code were you can get error,
# inside except write the message to print to user
# with except you can write the error type you can get.
# hear while loop will run until user gives right input. 
while True:
    try:
        user = int(input("Enter your age : "))

    except ValueError:
        print("You didnt entered a string... enter again...")
    except:
        print("Invalid input")
    # inside else you can write the your main functonal code 
    else:
        if user > 18:
            print("You can watch")
        else:
            print("You Cant..sorry")
        break
    # finally runs every time even if its exception
    finally:
        print("Finally its running everytime of execution")
            

# else finally clause 