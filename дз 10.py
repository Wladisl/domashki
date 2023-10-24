class Vehicle:
    brand = None
    year = None
    max_speed = None


class Car(Vehicle):
    seats = None

    def __init__(self, new_brand, new_year, new_speed, new_seats):
        self.brand = new_brand
        self.year = new_year
        self.max_speed = new_speed
        self.seats = new_seats

    def object_information(self):
        print(f'Car brand -> {self.brand}, year published -> {self.year}, max speed -> {self.max_speed} km/h, max seats -> {self.seats}')


class Airplane(Vehicle):
    wingspan = None

    def __init__(self, new_brand, new_year, new_speed, new_wingspan):
        self.brand = new_brand
        self.year = new_year
        self.max_speed = new_speed
        self.wingspan = new_wingspan

    def object_information(self):
        print(f'Airplane name -> {self.brand}, year published -> {self.year}, max speed -> {self.max_speed} km/h, max wingspan -> {self.wingspan}m')


class Ship(Vehicle):
    tonnage = None

    def __init__(self, new_brand, new_year, new_speed, new_tonnage):
        self.brand = new_brand
        self.year = new_year
        self.max_speed = new_speed
        self.tonnage = new_tonnage

    def object_information(self):
        print(f'Ship name -> {self.brand}, year published -> {self.year}, max speed -> {self.max_speed} m/s, max tonnage -> {self.tonnage} ton')


my_car = Car('Toyota', 2017, 230, 8)
my_car.object_information()

my_airplane = Airplane('F-16', 1974, 2120, 9.96)
my_airplane.object_information()

my_ship = Ship('Titanic', 1911, 23, 564763)
my_ship.object_information()
