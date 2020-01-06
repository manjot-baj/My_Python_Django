# In inheritance we can derive more then one class means
#  one parent class can have many child classes
# and this type of inheritance is called 
# multi-level inheritance
# ex :
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

    def full_name(self):
        return f"{self.brand} {self.model}"

class Smartphones(Phone): # derived / child class
    def __init__(self,brand,model,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
    @property
    def Smartspecification(self):
        return f"Brand : {self.brand}, Model : {self.model}, Ram : {self.ram}, Internal Space : {self.internal_memory}, Camera : {self.rear_camera} "

class Gaming_smartphones(Smartphones): # Another derived / child class
    def __init__(self,brand,model,price,processor,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model,price,ram,internal_memory,rear_camera)
        self.rear_camera = rear_camera
        self.front_camera = front_camera
        self.processor = processor
    @property
    def Gaming_specifications(self):
        return f"Brand : {self.brand}, Model : {self.model}, Processor : {self.processor}, Ram : {self.ram}, Internal Space : {self.internal_memory}, Rear Camera : {self.rear_camera}, front camera : {self.front_camera} "

Phone1 = Phone("Nokia","3310",500)
Phone2 = Smartphones("Samsung","j2",7500,"1gb","8gb","5mp")
Phone3 = Gaming_smartphones("Asus","ZenPro",25000,"Hellios-930","12gb","128gb","25mp","15mp")
print(Phone3.brand)
print(Phone3.model)
print(Phone3.price)
print(Phone3.specification)
print(Phone3.Smartspecification)
print(Phone3.Gaming_specifications)