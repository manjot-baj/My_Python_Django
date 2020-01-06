class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = max(price,0)
    @property
    def specification(self):
        return f"{self.brand} {self.model} {self.price}"
    # works as getter
    # gets the object with value
    @property
    def _price(self):
        return self.price
    # works as setter
    # sets the object with new_value
    @_price.setter
    def _price(self,new_price):
        self.price = max(new_price,0)
    
    def make_call(self,phone_no):
        print(f"Calling...{phone_no}")

    def full_name(self):
        return f"{self.brand} {self.model}"

p1 = Phone("samsung","j2",7500)

p1._price = 500
print(p1.price)
print(p1.specification)
