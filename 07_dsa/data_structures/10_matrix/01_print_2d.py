# Write a program to take input and print a 2D array.

# Python implementation
def print_2d_array(rows, cols):
    array = []
    for i in range(rows):
        row = list(map(int, input().split()))
        array.append(row)
    
    print("2D Array:")
    for row in array:
        print(" ".join(map(str, row)))

# Example usage
print_2d_array(3, 4)
