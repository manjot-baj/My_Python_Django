class Static_method:
    def __init__(self):
        print("This is instance method")
    @staticmethod
    def hello():
        print("This is hello() static method")
p1 = Static_method.hello()
p1 = Static_method()