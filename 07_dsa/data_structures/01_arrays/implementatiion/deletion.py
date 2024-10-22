
def delete_element(arr, index):
    if index < 0 or index >= len(arr):
        print("Invalid index")
        return
    
    # Shifting elements to the left to fill the gap
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]
    
    arr.pop()  # Decrease the size of the array

# Example usage
arr = [10, 20, 25, 30, 40]
delete_element(arr, 2)
print(arr)


# Time Complexity: O(n), because all elements after the deleted element have to be shifted.