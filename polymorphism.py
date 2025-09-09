class Bird:
    def make_sound(self):
        return "Chirp"
    
class Dog:
    def make_sound(self):
        return "Woof"

class Cat:
    def make_sound(self):
        return "Meow"
    
animals = [Bird(), Dog(), Cat()]

for animal in animals:
    print(animal.make_sound()) # same call, different behavior