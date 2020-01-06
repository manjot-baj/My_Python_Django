def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError as err:
        print(err)
    except TypeError:
        print("Number must be float or int")
    except:
        print("invalid input")
print(divide(10,12))
