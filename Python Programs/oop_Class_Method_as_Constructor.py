class Family:
    def __init__ (self,relation,name,age):
        self.relation = relation
        self.name = name
        self.age = age
    # class method as constructor
    @classmethod
    def from_string(cls,string):
        relation,name,age = string.split(",")
        # creating object of variable
        return cls(relation,name,age)
# calling our constructor
p1 = Family.from_string("Son,Manjot,21")
print(p1.relation)
print(p1.name)
print(p1.age)
