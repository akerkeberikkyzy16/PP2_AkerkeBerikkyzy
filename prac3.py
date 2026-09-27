class Car():
    def __init__(self, brand, y):
        self.brand = brand
        self.year = y
    def show_info(self):
        if self.year>=2020:
            print("Modern car")
        else:
            print("OLd car")
car=Car("Camry", 2014)
car.show_info()