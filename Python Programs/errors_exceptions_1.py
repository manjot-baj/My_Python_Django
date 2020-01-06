# raise keyword and raising our own errors
class Animal:
    def __init__(self,name):
        self.name = name
        return "This is Animal class"
        # this is abstract method
    def sound(self):
        raise NotImplementedError("You have not define method in subclass")
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        return "Bhow..Bhow..."
class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        return "Bhow..Bhow..."

dog = Dog("shiro","lambridon")
print(dog.sound())

    
    