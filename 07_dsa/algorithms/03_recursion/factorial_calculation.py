# Factorial Calculation
# Calculate the factorial of a non-negative integer n.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
print(factorial(5))
