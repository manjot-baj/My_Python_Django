# __str__ and __repr__
# dunder methods
class Phone: 
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = max(price,0)
# if user type 
# p1 = Phone("Nokia","3310",500)
# print(p1)
# then str function is called.
# __str__ method is used by user to see its object value
    def __str__(self):
        return f"{self.brand} {self.model} {self.price}"
# __repr__ method is used by developer for writing main functionality 
    def __repr__(self):
        return f"Phone(\"{self.brand}\",\"{self.model}\",\"{self.price}\")"
# len function for yoyr class 
    def __len__(self):
        return len(self.brand) + len(self.model)+len(str(self.price))
    
p1 = Phone("Nokia","3310",500)
print(p1)
print(repr(p1))
print(len(p1))

