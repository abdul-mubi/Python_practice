from extend_base_class import MyBaseClass
# import extend_base_class

class MyDerivedClass(MyBaseClass):
    def derived_method(self):
        print("This is a method from the derived class.")

obj1 = MyDerivedClass()
obj1.derived_method()
obj1.base_method()
obj2 = MyBaseClass()
obj2.base_method()