class Laptop:
    percent = 10
    def __init__ (self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price
        self.description = brand_name + " " + model_name + " " + str(price)
    
    def apply_discount(self):
        Discounted_price = self.percent * self.price / 100
        Final_price = self.price - Discounted_price
        print(f"your discounted price {Final_price} you will saved {Discounted_price} ")

pc = Laptop("Lenovo","g50",30000)
pc2 = Laptop("Lenovo","g50-gaming",80000)
pc2.percent = 15
pc2.apply_discount()

# here python will take class variable value by default
pc.apply_discount()

# suppose you have 10% off sale on all laptops 
# but for gaming laptops you want to keep 15% off.
# as class variable is constant and you have passed
#  percent = 10
# but you can change the discount for some products 
# by pc2.percent = 15
# object.class variable = new value
# but in defination of apply_discount() 
# change Class.Class varaible  to object.variable.
# means Laptop.percent to self.percent
# and suppose you dont assign new value to your percent.
# means you dont pass this
# object.class variable = new value.
# python will take class variable by default.