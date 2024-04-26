
# Agreegation vs Inheritance

# Aggregation (has a)
# customer has a address

# Inheritance (is a)
# smatphone is a product
# car is a vehicle



class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address


    def edit_profile(self, newName, newGender, newCity, newPin, newState):
            self.name = newName
            self.gender = newGender
            self.address.change_address(newCity, newPin, newState)


class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self, newCity, newPincode, newState):
        self.city = newCity
        self.pincode = newPincode
        self.state = newState


add = Address('Islamabad', 5500, 'Isl')
cust = Customer('Huchi', 'Male', add)

print(cust.address.pincode)

add.change_address('Lahore', 8900, 'Lhr')
print(add.city)

cust.edit_profile('raima', 'female', 'bhaipheru', 4589, 'bhp')
print(cust.name)
print(cust.address.city)