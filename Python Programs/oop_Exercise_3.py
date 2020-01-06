class Person:
    count = 0
    def __init__(self):
        Person.count += 1
    def Object_count(self):
        return Person.count

p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()
print(Person.Object_count(p1))


