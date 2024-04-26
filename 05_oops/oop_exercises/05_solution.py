class Car:

    def __init__(self, brand, model):
        self.__brand = brand        #private instance variable
        self.__model = model        #private instance variable
        

    def full_name(self):
        return f"{self.__brand} : {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"



my_honda = Car('Honda', 'Civic Turbo')
print(my_honda.fuel_type())

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.fuel_type())

