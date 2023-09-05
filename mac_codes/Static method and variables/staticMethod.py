class StaticClass():
    def __init__(self):
        print('Creating object for StaticClass and initializing self variables if any')
    
    #In python all variables defined at class level are static variables
    static_var_a = 'static_var_a'
    _protected_var = 'protected_var'
    __private_var = 'private_var'

    @staticmethod
    def static_method():
        print('inside static method')
        cert_location = 'c/window/certification/device'
        return cert_location
    
    def non_static_method(self):
        print('inside non-static method')

    def call_private_var(self):
        print(self.__private_var)

StaticClass.static_method()
print(StaticClass.static_var_a)
print(StaticClass._protected_var)
print(StaticClass.__private_var) #AttributeError: type object 'StaticClass' has no attribute '__private_var'

obj1 = StaticClass()
obj1.static_method()
obj1.non_static_method()
obj1.call_private_var()