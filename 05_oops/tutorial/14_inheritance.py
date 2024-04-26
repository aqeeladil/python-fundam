############################### inheritance ###############################

# class Parent:
#     pass

# class Child(Parent):
#     pass

############################### inheriting constructor ###############################

# class Phone:
#     def __init__(self, price, brand, camera):
#         print('Inside phone constructor')
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')


# class smart_phone(Phone):
#     pass

# s = smart_phone(20000, 'Apple', 14)



############################### inheriting private members ###############################

# class Phone:
#     def __init__(self, price, brand, camera):
#         print('Inside phone constructor')
#         self.price = price
#         self.__brand = brand
#         self.camera = camera


# class smart_phone(Phone):
#     pass

# s = smart_phone(20000, 'Apple', 14)
# print(s.__brand)        #this code will not work bcz we cannot inherit the private variable


################################# Medhod Overriding (polymorphism) ########################################

# class Phone:
#     def __init__(self, price, brand, camera):
#         print('Inside phone constructor')
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')


# class smart_phone(Phone):
#     def buy(self):
#         print('Buying a smartphone')

# s = smart_phone(20000, 'Apple', 14)
# s.buy()             # it will execute smart_phone's buy() function

# # above is example of method overriding


################################ getting a private variable from parent class ###########################

# class Parent:
#     def __init__(self, num):
#         self.__num = num
    
#     def get_num(self):
#         return self.__num
    
# class Child(Parent):
#     def show(self):
#         print('This is child class')

# son = Child(100)
# print(son.get_num())
# son.show()


################################ Example 2 ##################################

# class Parent:
#     def __init__(self, num):
#         self.__num = num
    
#     def get_num(self):
#         return self.__num
    
# class Child(Parent):
#     def __init__(self, val, num):
#         self.__val = val

#     def get_val(self):
#         return self.__val

# son = Child(2, 3)
# print('Parent Num', son.get_num())
# print('Child Val', son.get_val())

# # this code will throw error
# # bcz if child constructor is present, then you cannot directly call parent constructor


#################################### Example 3 ###############################

# class A:
#     def __init__(self):
#         self.var1 = 100

#     def display1(self, var1):
#         print('Class A', self.var1)

# class B(A):
#     def display2(self, var1):
#         print('Class B', self.var1)

# obj = B()
# obj.display1(200)

################################### super method ####################################

# class Phone:
#     def __init__(self, price, brand, camera):
#         print('Inside phone constructor')
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')


# class smart_phone(Phone):
#     def buy(self):
#         print('Buying a smartphone')
#         super().buy()

# s = smart_phone(20000, 'Apple', 14)
# s.buy()


############################### super constructor #################################

# class Phone:
#     def __init__(self, price, brand, camera):
#         print('Inside phone constructor')
#         self.price = price
#         self.brand = brand
#         self.camera = camera


# class smart_phone(Phone):
#     def __init__(self, price, brand, camera, os, ram):
#         super().__init__(price, brand, camera)
#         self.os = os
#         self.ram = ram
#         print('Inside the smartPhone constructor')


# s = smart_phone(20000, 'Apple', 14, 'iOs', 8)
# print(s.os)
# print(s.brand)



########################## Example on super() ######################

# class Parent:
#     def __init__(self, num):
#         self.__num = num
    
#     def get_num(self):
#         return self.__num
    
# class Child(Parent):
#     def __init__(self, val, num):
#         super().__init__(num)
#         self.__val = val

#     def get_val(self):
#         return self.__val

# son = Child(2, 3)
# print('Parent Num', son.get_num())
# print('Child Val', son.get_val())


########################### example 2 on super() ######################

# class Parent:
#     def __init__(self):
#         self.num = 100
    
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.val = 200

#     def show(self):
#         print(self.num)
#         print(self.val)


# son = Child()
# son.show()


################################## Example 3 on super() #############################

# class Parent:
#     def __init__(self):
#         self.__num = 100

#     def show(self):
#         print('Parent', self.__num)
        
    
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__val = 200

#     def show(self):
#         print('Child', self.__val)
        

# dad = Parent()
# dad.show()
 
# son = Child()
# son.show()


################################# Method Resolution Order ################################

# class Phone:
#     def __init__(self, price, brand, camera):
#         print('Inside phone constructor')
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')


# class Product:
#     def buy(self):
#         print('Product buy method')

# class smart_phone(Product, Phone):       # here product class will be executed first, this is method resolution order
#     pass

# s = smart_phone(20000, 'Apple', 14)
# s.buy()
