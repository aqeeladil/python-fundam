class Customer:
        
    def __init__(self, name):
        self.name = name
        

def greet(customer):
    print(id(customer))


cust1 = Customer('Aqeel')
print(id(cust1))

greet(cust1)


# here we get same id values