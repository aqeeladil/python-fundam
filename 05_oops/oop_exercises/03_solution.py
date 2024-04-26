class Car:

    def __init__(self, brand, model):
        self.brand = brand        #instance variable
        self.model = model        #instance variable
        

    def full_name(self):
        return f"{self.brand} : {self.model}"
    


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size



my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(my_tesla.full_name())
print(my_tesla.battery_size)