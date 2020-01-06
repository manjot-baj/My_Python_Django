
def Prime(number):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                return "Not Prime"
        return "Prime"

User = int(input(" Enter any Number : "))
print(Prime(User))
     