# Fibonacci function
def Fibonacci_Seq(n):
    Firstno=0
    Secondno=1
    if n == 1:
        print (Firstno)
    elif n == 2:
        print(Firstno,Secondno)
    else:
        print (Firstno,Secondno,end=" ")
        for i in range(n-2):
            a= Firstno + Secondno
            Firstno = Secondno
            Secondno = a
            print(Secondno,end=" ")

user=int(input("Enter the nth number for fibonacci series : "))
Fibonacci_Seq(user)