# Palindrome Program
a=input("String for palindrome check: ")
a1= a.replace(" ","")
n= (a1[::-1])
if a1.lower() == n.lower():
    print(f"The given string {a1} is palindrome ") 
else:
    print(f"The given string {a1} is not a palindrome") 