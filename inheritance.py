class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return "Moving fordward"

class Car(Vehicle): # inherits from vehicle
    def honk(self):
        return "Beep beep!"
    
my_car = Car("Toyota")
print(my_car.brand)  # Inherited from Vehicle
print(my_car.drive()) # Inherited method
print(my_car.honk()) # Car's own method