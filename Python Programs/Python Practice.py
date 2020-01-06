# no1,no2,no3 = map (input("enter 3 no with commos"))
num1, num2, num3 = map( int, input("Enter three integer numbers separated by comma : ").split(","))
avg=(num1+num2+num3)/3
print(f"Average is{avg}")