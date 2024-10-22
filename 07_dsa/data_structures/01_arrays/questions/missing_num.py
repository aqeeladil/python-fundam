# Find the missing number in an array of size n containing numbers from 1 to n+1


def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

arr = [1, 2, 4, 5]
missing_number = find_missing_number(arr)
print(missing_number)

