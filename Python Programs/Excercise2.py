# Excercise for practice
name,char=map(str,input("Enter name and char : ").split(","))
n=name.strip(" ")
l=len(n)
lowername=n.lower()
lowerchar=char.lower().strip(" ")
c=lowername.count(lowerchar)
print(f"The length of the name is {l} and the count of char is {c}")