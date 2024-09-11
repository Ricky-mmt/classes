class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def start_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} is now running.")

    def stop_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} has been turned off.")

    def drive(self):
        print(f"The {self.color} {self.make} {self.model} is now driving.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model} in {self.color}"

# Example usage
car1 = Car("Toyota", "Corolla", 2020, "blue")
car2 = Car("Honda", "Civic", 2019, "red")

car1.start_engine()
car1.drive()
car1.stop_engine()

print(car1.get_info())
print(car2.get_info())
