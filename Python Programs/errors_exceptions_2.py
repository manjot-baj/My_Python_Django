class Mobile:
    def __init__(self,name):
        self.name = name
class MobileStore:
    def __init__(self):
        self.mobiles = []
    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
            return self.mobiles
        else:
            raise TypeError("You should make object of Mobile class before passing inside addMobile method")
VijaySales = Mobile("Samsung Galaxy j2")
mobo = MobileStore()
print(mobo.add_mobile(VijaySales))
print(mobo.add_mobile("VijaySales"))