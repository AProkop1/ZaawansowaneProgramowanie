class Property:
    def __init__(self, area: str, rooms: int, price: int, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House is located in {self.area} on {self.address}, has {self.rooms} rooms and cots {self.price}. "\
               f"Its plot is equal to {self.plot}"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat is located in {self.area} on {self.address}, has {self.rooms} rooms and cots {self.price}. "\
               f"It's on {self.floor} flor."


my_house = House('Białołęka', 7, 7, "Bohaterów 67", 2)
my_flat = Flat("Praga", 3, 900000, "Ratuszowa 13/4", 2)

print(my_house)
print(my_flat)

