year = int(input())  # we take year as input and convert into interger.

if year % 4 == 0:  # we check if year is divisible by 4 or not
    if year % 100 == 0:  # then we check year is divisible by 100 or not
        if year % 400 == 0:  # check year is divisible by 400 or not
            print(str(year) + " is leap year")  # all condition are satified hence year is leap year
    #         # we convert year integer into string and concat with message
        else:
            print(str(year) + " is not leap year")  # if year is divisible by 100 but not 400 then it is not leap year
    else:
        print(str(year) + " is leap year")  # if year is divisible by 4 but not 100 then it is leap year
else:
    print(str(year) + " is not leap year")  # if year is not divisible by 4 then it is not leap year
