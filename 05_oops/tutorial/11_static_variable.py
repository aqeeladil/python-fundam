class Atm:
    # static variable
    counter = 1

    def __init__(self):
        # instance variable
        self.__pin = ''
        self.__balance = 0
        self.sno = Atm.counter
        Atm.counter = Atm.counter + 1


c1 = Atm()
c2 = Atm()
c3 = Atm()

print(c1.sno)
print(c2.sno)
print(c3.sno)

print(c1.counter)
print(c2.counter)
print(c3.counter)

print(Atm.counter)
        