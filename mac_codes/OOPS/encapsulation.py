#Access modifiers
class Car:
    def __init__(self, make, model):
        self._make = make           # Protected attribute with a single leading underscore, Protected means that the attribute/method can only be used in the class where it is defined or its subclass
        self.__model = model        # Private attribute with two leading underscores, private means that the attribute/method can only be used inside the class where it is defined

    def get_make(self):
        return self._make

    def set_make(self, new_make):
        self._make = new_make

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        self.__model = new_model

    def __private_method(self):
        print('inside private method')
    
    def _protected_method(self):
        # self.__private_method()
        print('inside protected method')

# Creating an instance of the Car class
car1 = Car("Toyota", "Corolla")

car1._protected_method()
car1.__private_method() # Raises an AttributeError: 'Car' object has no attribute '__private_method'.


# Accessing and modifying attributes using public methods
print(car1.get_make())         # Output: Toyota
car1.set_make("Honda")
print(car1.get_make())         # Output: Honda

# Attempting to access the protected attribute directly raises an AttributeError
print(car1.__model)           # Raises an AttributeError
print(car1._make)

# Accessing and modifying protected attributes using public methods
print(car1.get_model())        # Output: Corolla
car1.set_model("Civic")
print(car1.get_model())        # Output: Civic
