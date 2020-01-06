# Palindrome Function
def palindrome(userword):
    reverseword= userword[::-1]
    if userword.lower() ==  reverseword.lower():
        return  True
    return False

a=input("String for palindrome check: ")
a1= a.replace(" ","")
a2=palindrome(a1) #Palindrome Function called
print(f"Palindrome Condithion is {a2}")