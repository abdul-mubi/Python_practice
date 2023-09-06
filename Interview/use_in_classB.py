#Create a var in class A and use that in class B
class A():
    def __init__(self):
        self.a = 'i am inside A'

class B(A):
    def __init__(self):
        # super().__init__()
        A.__init__(self)
        self.b = 'i am inside B'

    def func(self):
        print(self.a)

obj1 = B()
obj1.func()