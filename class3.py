

class Departure:
    def __init__(self, departure_city, destination_city, flight_number, departure_time):
        self.departure_city = departure_city
        self.destination_city = destination_city
        self.flight_number = flight_number
        self.departure_time = departure_time

    def display_info(self):
        print(f"Flight {self.flight_number} from {self.departure_city} to {self.destination_city} departs at {self.departure_time}.")

