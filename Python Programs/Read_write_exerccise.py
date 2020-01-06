with open("salary.txt","r") as sal_file:
    with open("user.txt","a") as user_file:
        for line in sal_file.readlines():
            name,salary = line.split(",")
            user_file.write(f"{name}\'s salary is {salary}")
