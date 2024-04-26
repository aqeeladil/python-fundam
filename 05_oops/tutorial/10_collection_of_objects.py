class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
c1 = Customer('Aqeel', 25)
c2 = Customer('Asad', 31)
c3 = Customer('Shan', 33)

list = [c1, c2, c3]

for item in list:
    print(item.name, item.age)