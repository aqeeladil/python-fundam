# Method Overloading
# Method Overloading: here we can induce different behaviours from the same method by giving different inputs
# this concept is little different in python as compared to other languages like java
# technically speaking, this kind of overloading does not work
# we use other technique to achieve the result


############################# typical overloading method used in java ####################

class Geometry:
    def area(self, radius):
        return 3.14 * radius * radius
    
    def area(self, l, b):
        return l * b
    

obj = Geometry()
#print(obj.area(4))   
#print(obj.area(4, 5))

#this code will not work in python


######################### method overloading in python ########################

class Geometry:
    def area(self, a, b=0):
        if (b==0):
            print('Circle', 3.14 * a * a)
        else:
            print('Rectangle', a * b)
    

# obj = Geometry()
# obj.area(4)
# obj.area(4, 5)

