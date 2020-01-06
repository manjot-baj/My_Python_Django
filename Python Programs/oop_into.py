# for convention always write class name first alphabet in caps.
class Family:
    # init is a constructor in python
    def __init__ (self,relation,name,age):
        # for convention write self
        # self means p1 
         # instance variables
        self.relation = relation
        self.name = name
        self.age = age

p1 = Family("father","Satpal",44)
print(p1.name)
print(p1.relation)
print(p1.age)
    
    