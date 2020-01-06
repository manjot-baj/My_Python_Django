# method overriding
class Phone: # base / parent class
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = max(price,0)
    @property
    def specification(self):
        return f"{self.brand} {self.model} {self.price}"

    def make_call(self,phone_no):
        print(f"Calling...{phone_no}")
    @property
    def full_name(self):
        return f"{self.brand} {self.model}"

class Smartphones(Phone): # derived / child class
    def __init__(self,brand,model,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
    @property
    def full_name(self):
        return f"Brand : {self.brand}, Model : {self.model}, Ram : {self.ram}, Internal Space : {self.internal_memory}, Camera : {self.rear_camera} "

class Gaming_smartphones(Smartphones): # Another derived / child class
    def __init__(self,brand,model,price,processor,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model,price,ram,internal_memory,rear_camera)
        self.rear_camera = rear_camera
        self.front_camera = front_camera
        self.processor = processor
    # @property
    # def full_name(self):
    #     return f"Brand : {self.brand}, Model : {self.model}, Processor : {self.processor}, Ram : {self.ram}, Internal Space : {self.internal_memory}, Rear Camera : {self.rear_camera}, front camera : {self.front_camera} "
Phone1 = Phone("Nokia","3310",500)
Phone2 = Smartphones("Samsung","j2",7500,"1gb","8gb","5mp")
Phone3 = Gaming_smartphones("Asus","ZenPro",25000,"Hellios-930","12gb","128gb","25mp","15mp")
print(Phone3.full_name)
# Method resolution
# In Python to see methd resolution of a class
# type help(classname)
# ex :
# print(help(Gaming_smartphones))
# method resolution for Gaming_smartphones
#  |  Method resolution order:
#  |      Gaming_smartphones
#  |      Smartphones
#  |      Phone
#  |      builtins.object
# if your object of class gaming smartphones calls any method 
# then python will search for method according to that class
# method resolution order
# means python will search for method first in that class if 
# its not available then next class in method resolution order 
# of Gamingsmartphone
# builtinsobject is a class in python
# if you create a class in python 
# you by default inherit that class from bultinsobject 

# isinstance() and issubclass() methods
print(isinstance(Phone3,Gaming_smartphones))
# this method tells that whether this object is of this class
print(issubclass(Gaming_smartphones,Phone))
# this method tells that whether this class is a subclass of this class
 