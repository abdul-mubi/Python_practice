# Method overloading is not possible in python but we can achieve the same behaviour using default variable

class adding():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self,c=0):
        print(self.a + self.b + c)
    
obj1 = adding(8, 9)
obj1.add()
obj1.add(10)

