# for convention always write class name first alphabet in caps.
class Laptop:
    # init is a constructor in python
    def __init__ (self,brand_name,model_name,price):
        # for convention write self
        # self means p1 
        # instance variables 
        self.brand = brand_name
        self.model = model_name
        self.price = price
        self.description = brand_name + " " + model_name + " " + str(price)
        
pc = Laptop("Lenovo","g50",30000)
print(pc.brand)
print(pc.model)
print(pc.price)
print(pc.description)