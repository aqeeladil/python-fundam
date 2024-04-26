class Customer:
        
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


cust1 = Customer('Aqeel', 'Male')

###################################################

# pass by refernce 
def greet(customer):
    if (customer.gender == 'Male'):
        print('hello',  customer.name, 'sir')
    else:
        print('hello',  customer.name, 'maam')


    cust2 = Customer('Raima', 'Female')
    return cust2

greet(cust1)

# returning a value
new_cust = greet(cust1)
print(new_cust.name)