class School:
    def __init__(self, name, location, school_type, num_students):
        self.name = name
        self.location = location
        self.school_type = school_type
        self.num_students = num_students

    def display_info(self):
        print(f"School Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Type: {self.school_type}")
        print(f"Number of Students: {self.num_students}")
