class monkey_patching():
    a = 1
    def original_method(self):
        print('i am inside original method')

obj = monkey_patching()
obj.original_method()
print(monkey_patching.a)

def new_method(self):
    print('inside new method')

# Monkey patching: Replace the original method with the new method
monkey_patching.original_method = new_method
monkey_patching.a = 100

obj.original_method()
print(monkey_patching.a)



