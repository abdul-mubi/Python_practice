from baseclass import BaseClass

class SubClass(BaseClass):
    def __init__(self, one,two,third):
        super().__init__(one, two)
        self.third = third

    def inside_sub(self):
        print(self.two)
        print(self.third)
        self.two = 4
        print(self.two)

obj1 = SubClass(1,2,3)
# print(obj1.a)
obj1.abs()
obj1.inside_sub()
print(obj1.two)




