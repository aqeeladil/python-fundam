
# Everything in python is an Object
 
# Object, Class, Encapsulation, Abstraction, Inheritance, Polymorphism

# An object is an instance of a class
* objects are mutable

# Function vs Method
* A method is a special function which is called inside a Class
* Function Example :
len(list)
* Method Example :
* huchi.append(list)    # any function with dot feature is a method


# Constructor __init__
* it is a special method that automatically gets exectued when a new object is created (when the class is called)
* special methods in python are called Magic/dunder methods.
* an object itself directly cannot call a magic method.
* 'self' keyword refers to the object
* one method in class cannot access other methods. it is possible only through 'self' parameter, which refers to the object


# Encapsulation
* Instance variable is a variable whose value is different for d/f objects

* private variable (not easily accessible from outside of class)
two underscores in front of varible
example; __pin, __balance
* getter & setter

# Reference Variable
* a reference variable is a variable which refers to the actual object
* example; in the below example, the variable 'meezan' is a reference variable
meezan = Atm()


# Static variable
* static variable is one whose value remains static for all the objects made by a class
* static methods dont need self parameter


# Agreegation vs Inheritance
* Aggregation (has a)
customer has a address

* Inheritance (is a)
smatphone is a product
car is a vehicle


# Inheritance
* DRY (do not repeat yourself)
* private variables and static methods are not inherited

# Polymorphism
* means multiple faces
* three types
method overriding
method overloading
operator overloading

# Inheritance Types
Single
Multiple
Multilevel
Hierarcial
Hybrid



# Method Overloading
* Method Overloading: here we can induce different behaviours from the same method by giving different inputs
* this concept is little different in python as compared to other languages like java
* technically speaking, this kind of overloading does not work
* we use other technique to achieve the result