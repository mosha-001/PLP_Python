# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._battery = 100       # protected attribute
        self.__serial_number = "SN12345"  # private attribute

    def charge(self, amount):
        self._battery = min(100, self._battery + amount)
        print(f"{self.model} charged to {self._battery}%")

    def get_serial_number(self):  # encapsulated access
        return self.__serial_number


# Child class inheriting Device
class Smartphone(Device):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = os

    def use_app(self, app, battery_use):
        if self._battery > battery_use:
            self._battery -= battery_use
            print(f"Using {app} on {self.model}... Battery left: {self._battery}%")
        else:
            print("Battery too low! Please charge.")


# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S22", "Android")
phone2 = Smartphone("Apple", "iPhone 14", "iOS")

# Demonstration
phone1.use_app("YouTube", 20)
phone2.use_app("Instagram", 40)
phone1.charge(30)
print("Serial Number:", phone1.get_serial_number())  # accessing private attribute via method

class Car:
    def move(self):
        print("🚗 Driving on the road...")

class Plane:
    def move(self):
        print("✈️ Flying in the sky...")

class Boat:
    def move(self):
        print("🚤 Sailing on the water...")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
