from abc_module import check_abc

class imple_abc_module(check_abc):
    def my_own_method(self):
        print('Inside my_own_method')
    
    def my_abstract_method(self):
        print('this is my_abstract_method inside imple_abc_module')

obj1 = imple_abc_module()
obj1.my_own_method()
obj1.my_abstract_method()
obj1.my_concrete_method()