class Fraction:
    def __init__(self, n, m):
        self.num = n
        self.den = m

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    
    def __add__(self, other):
        temp_num = (self.num * other.den) + (other.num * self.den)
        temp_den = self.den * other.den
        return f"{temp_num}/{temp_den}"
    
    def __sub__(self, other):
        temp_num = (self.num * other.den) - (other.num * self.den)
        temp_den = self.den * other.den
        return f"{temp_num}/{temp_den}"
    
    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return f"{temp_num}/{temp_den}"
    
    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return f"{temp_num}/{temp_den}"


    
x = Fraction(4, 5)
# print(x)

y = Fraction(1, 2)
# print(y)

addition = x + y
# print(addition)

subtraction = x - y
# print(subtraction)

multiplication = x * y
print(multiplication)

division = x / y
print(division)
