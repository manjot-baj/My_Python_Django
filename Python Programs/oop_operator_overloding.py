class Phone: 
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = max(price,0)
    def __add__(self,other):
        return self.price + other.price
p1 = Phone("Nokia","3310",500)
p2 = Phone("Nokia","3310",500)
print(p1+p2)
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