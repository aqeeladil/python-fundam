# List comp with functions
def square(x):
    return x**2


sqr_nums = [square(x) for x in range(10)]

print(sqr_nums)