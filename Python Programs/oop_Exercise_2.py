class Laptop:
    def __init__ (self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price
        self.description = brand_name + " " + model_name + " " + str(price)
    
    def apply_discount(self,percent):
        Discounted_price = percent * self.price / 100
        Final_price = self.price - Discounted_price
        print(f"your discounted price {Final_price} you will saved {Discounted_price} ")

pc = Laptop("Lenovo","g50",30000)
pc2 = Laptop("Lenovo","g50-gaming",80000)
print(pc.description)
pc.apply_discount(10)
pc2.apply_discount(25)