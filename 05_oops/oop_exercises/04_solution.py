class Car:

    def __init__(self, brand, model):
        self.__brand = brand        #private instance variable
        self.__model = model        #private instance variable
        

    def full_name(self):
        return f"{self.__brand} : {self.__model}"
    
    def get_brand(self):
        return self.__brand
    


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size



my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(my_tesla.get_brand())