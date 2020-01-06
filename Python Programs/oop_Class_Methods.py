class Person:
    count = 0
    def __init__(self):
        Person.count += 1
# Class method 
# step 1 : call decorator classmethod
# def method with parameter as class for convention write cls
    @classmethod
    def Instance_count(cls):
        return cls.count

p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()
print(Person.Instance_count())