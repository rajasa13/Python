class Person:
    def __init__(self, name, age):
        self.name = name # public attribute
        self._age = age # "protected" by convention (single underscore)

    def introduce(self):
        return f"My name is {self.name} and I am {self._age} years old."
    
p1 = Person("Alice", 30)
print(p1.introduce())