# The primary purpose of __new__ is to create and return a new instance of a class.
# The __init__ method is responsible for initializing the object.

class SingletonClass(object):
    def __new__(cls):
        print("inside __new__ method")
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        print("inside __init__ method")
        self.check_init_val = 123
        # python doesnt allow us to use "return" keyword inside __init__ method
        # but we can use return keyword in __new__ method

singleton = SingletonClass()
print("--------------------------------")
new_singleton = SingletonClass()

print(singleton is new_singleton)

singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)

