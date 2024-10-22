# Rotate a matrix by 90 degrees clockwise.

def rotate_90_degrees(matrix):
    matrix = transpose(matrix)
    for row in matrix:
        row.reverse()
    return matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotated_matrix = rotate_90_degrees(matrix)
for row in rotated_matrix:
    print(row)
