

def update_element(arr, index, new_value):
    if index < 0 or index >= len(arr):
        print("Invalid index")
        return
    
    arr[index] = new_value

# Example usage
arr = [10, 20, 30, 40]
update_element(arr, 2, 35)
print(arr)


# Time Complexity: O(1), because array indexing allows direct access to any element.