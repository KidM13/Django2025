class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def info(self):
        print(f"Brand: {self.brand}, Year: {self.year}, Model: {self.model}")



v = Vehicle("Toyota", 2005)
c = Car("BMW", 2018, "X5")

v.info()   
c.info()   
