class Bird():
    def intro(self):
        print('There are many types of birds.')
    def fly(self):
        print('Any bird can fly')

class Parrot(Bird):
    def fly(self):
        print('parrot can also fly')

#Class name can be start with small letter
class ostrich(Bird):
    def fly(self):
        print('ostrich can also fly')

bird_obj = Bird()
parrot_obj = Parrot()
ostrich_obj = ostrich()

bird_obj.fly()
parrot_obj.fly()
ostrich_obj.fly()