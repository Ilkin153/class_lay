class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def start(self):
        print(self.brand, self.model, self.year)
    def stop(self):
        print(self.brand, self.model, self.year)

car1 = Car("Mercedes", "c250", 2020)
car2 = Car("Toyota", "camry", 2018)
car3 = Car("Hyunadai", "Accent", 2012)

car1.start()
car1.stop()

car2.start()
car2.stop()

car3.start()
car3.stop()