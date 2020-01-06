# circle
# area = pi r square
# circumference = 2 pi r
class Circle:
    """ Circle class...has methods area  and circumference of circle  """
    # Class Variable
    # Class variable is used when the variable value is constant
    pi = 3.14
    def __init__ (self,radius):
        self.radius = radius
    def area(self):
        """ inside Circle class...Gives area of circle  """
        return Circle.pi * self.radius**2
    def circumference(self):
         """ inside Circle class...Gives circumference of circle  """
        return 2 * Circle.pi * self.radius

C1 = Circle(5)
print(C1.area())
