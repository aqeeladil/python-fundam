class Atm:
    # static variable
    __counter = 1

    def __init__(self):
        # instance variable
        self.__pin = ''
        self.__balance = 0
        self.sno = Atm.__counter
        Atm.__counter = Atm.__counter + 1

    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new_counter):
        if type(new_counter) == int:
            Atm.__counter = new_counter
        else:
            print('Not Allowed')


c1 = Atm()

print(c1.sno)
print(c1.get_counter())

c1.set_counter(7)
print(c1.get_counter())       