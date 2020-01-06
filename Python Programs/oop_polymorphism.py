# Polymorphism means having more than one form of a single thing.
# method overriding
class Phone:  # base / parent class
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = max(price, 0)

    @property
    def specification(self):
        return f"{self.brand} {self.model} {self.price}"

    def make_call(self, phone_no):
        print(f"Calling...{phone_no}")

    @property
    def full_name(self):
        return f"{self.brand} {self.model}"


class Smartphones(Phone):  # derived / child class
    def __init__(self, brand, model, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    @property
    def full_name(self):
        return f"Brand : {self.brand}, Model : {self.model}, Ram : {self.ram}, Internal Space : {self.internal_memory}, Camera : {self.rear_camera} "


class Gaming_smartphones(Smartphones):  # Another derived / child class
    def __init__(self, brand, model, price, processor, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model, price, ram, internal_memory, rear_camera)
        self.rear_camera = rear_camera
        self.front_camera = front_camera
        self.processor = processor
    # @property
    # def full_name(self):
    #     return f"Brand : {self.brand}, Model : {self.model}, Processor : {self.processor}, Ram : {self.ram}, Internal Space : {self.internal_memory}, Rear Camera : {self.rear_camera}, front camera : {self.front_camera} "


Phone1 = Phone("Nokia", "3310", 500)
Phone2 = Smartphones("Samsung", "j2", 7500, "1gb", "8gb", "5mp")
Phone3 = Gaming_smartphones("Asus", "ZenPro", 25000, "Hellios-930", "12gb", "128gb", "25mp", "15mp")
print(Phone3.full_name)


# method overloading
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = max(price, 0)

    def __add__(self, other):
        return self.price + other.price


p1 = Phone("Nokia", "3310", 500)
p2 = Phone("Nokia", "3310", 500)
print(p1 + p2)
# operator overloader functions
# object.__add__(self,other)
# object.__sub__(self,other)
# object.__mul__(self,other)
# object.__matmul__(self,other)
# object.__truediv__(self,other)
# object.__floordiv__(self,other)
# object.__mod__(self,other)
# object.__divmod__(self,other)
# object.__pow__(self,other)
# object.__lshift__(self,other)
# object.__rshift__(self,other)
# object.__and__(self,other)
# object.__xor__(self,other)
# object.__or__(self,other)
