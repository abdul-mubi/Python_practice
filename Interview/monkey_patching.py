class monkey_patching():
    def original_method(self):
        print('i am inside original method')

obj = monkey_patching()
obj.original_method()

def new_method(self):
    print('inside new method')

# Monkey patching: Replace the original method with the new method
monkey_patching.original_method = new_method

obj.original_method()



