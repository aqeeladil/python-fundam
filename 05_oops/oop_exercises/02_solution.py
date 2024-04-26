class Car:

    def __init__(self, brand, model):
        self.brand = brand        # instance variable
        self.model = model        # instance variable
        

    def full_name(self):
        return f"{self.brand} : {self.model}"
    


my_car = Car('Toyota', 'GLI')
print(my_car.full_name())


        