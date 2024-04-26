class Car:

    total_car = 0      #class variable

    def __init__(self, brand, model):
        self.__brand = brand        #private instance variable
        self.__model = model        #private instance variable
        Car.total_car += 1           
        

    def full_name(self):
        return f"{self.__brand} : {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"



print(Car.general_description())


