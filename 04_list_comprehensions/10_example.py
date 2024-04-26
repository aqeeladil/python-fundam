# Generator comprehensions

# sum_of_squares = sum([x**2 for x in range(1000000)])    # inefficient code, as it stores all the values in memory and then sums it

sum_of_squares = sum(x**2 for x in range(1000000))

print(sum_of_squares)
