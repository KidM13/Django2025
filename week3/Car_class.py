class Car:
    def __init__(self,make):
        self.make=make
    
    def get_make(self):
        return self.make
    

car=Car("BMW")
print(car.get_make())