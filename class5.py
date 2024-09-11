class Boat:
    def __init__(self, name, boat_type, length, capacity):
        self.name = name
        self.boat_type = boat_type
        self.length = length
        self.capacity = capacity

    def display_info(self):
        print(f"Boat Name: {self.name}")
        print(f"Type: {self.boat_type}")
        print(f"Length: {self.length} feet")
        print(f"Capacity: {self.capacity} people")