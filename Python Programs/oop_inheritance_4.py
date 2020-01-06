# Multiple Inheritance
class A:
    def classa(self):
       return "This is Class A"
    @property
    def Hello(self):
        print("This is Class A method Hello()")
class B:
    def classb(self):
       return "This is Class B"
    @property
    def Hello(self):
        print("This is Class B method Hello()")
        
class C(A,B):
    pass

p1 = C()
print(isinstance(p1,B))