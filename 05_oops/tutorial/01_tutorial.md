## NAMING CONVENTION

* these doesnt exist in python, but are a good practice to follow
* by default, they are public

# private method
* "__name"
* means no one should access this outside of class
* but you can still access the private variable like in below example
obj = Student(21,"Harry") 
print(obj._Student__age)

# calling by object of class Student
print(obj._Student__age)

# protected method
* "_name"
* means only class and its subclasses should access it outside of class


###############################################################################


## STATIC METHODS
* static methods are example of decorators
* Static methods in Python are methods that belong to a class rather than an instance of the class.
* static method doesnot need "self" argument
* Example

class Math:
    @staticmethod
    def add(a, b):
        return a + b
result = Math.add(1, 2)
print(result) # Output: 3



##########################################################################


## CLASS VARIABLES  vs  INSTANCE VARIABLES

* Class variables are shared among all instances. They are defined outside of any method and are usually used to store information that is common to all instances of the class.
* It's also worth noting that, in python, class variables are defined outside of any methods and don't need to be explicitly declared as class variable. They are defined in the class level and can be accessed via classname.varibale_name or self.class.variable_name.

* Instance variables are unique to each instance of a class and are used to store information that is specific to each instance. They are defined inside the init method and are usually used to store information that is specific to each instance of the class.
* But instance variables are defined inside the methods and need to be explicitly declared as instance variable by using self.variable_name.



######################################################################

## CLASS METHODS

* A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class. Class methods are defined using the "@classmethod" decorator, followed by a function definition. The first argument of the function is always "cls," which represents the class itself.

* It's important to note that class methods cannot modify the class in any way. If you need to modify the class, you should use a class level variable instead.

* They are useful for creating factory methods, alternative constructors, and other types of methods that operate at the class level. With the knowledge of how to define and use class methods, you can start writing more complex and organized code in Python.



################################################################

## dict, dir(), help()

* In Python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help()

* dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object. 
Example:
x = [1, 2, 3]
dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


* __dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection. 
Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)
p.__dict__
{'name': 'John', 'age': 30}   #Output


* help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods. 
Example:
help(str)


#########################################################################

