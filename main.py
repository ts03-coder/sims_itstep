class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers_names(self):
        count_passengers = 0
        if self.passengers != []:
            print(f"Names of {self.brand} passengers: ")
            for passenger in self.passengers:
                print(passenger.name)
                count_passengers += 1
            print(f"Кількість пасажирів {count_passengers}")
        else:
            print(f"There are no passenger in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
anton = Human("Anton")
car = Auto("Mercedes")

car.add_passenger(nick, kate, anton)

car.print_passengers_names()