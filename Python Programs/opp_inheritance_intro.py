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

    def full_name(self):
        return f"{self.brand} {self.model}"


class Smartphones(Phone):  # derived / child class
    def __init__(self, brand, model, price, ram, internal_memory, camera):
        super().__init__(brand, model, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.camera = camera

    @property
    def Smartspecification(self):
        return f"Brand : {self.brand} Model : {self.model} Ram : {self.ram} Internal Space : {self.internal_memory} Camera : {self.camera} "


Phone1 = Smartphones("Samsung", "j2", 7500, "1gb", "8gb", "5mp")
Phone2 = Phone("Nokia", "3310", 500)
print(Phone1.Smartspecification)
print(Phone1.brand)
print(Phone1.model)
print(Phone1.price)
Phone1.make_call(9922620357)
print(Phone1.specification)
print(Phone1.full_name())
