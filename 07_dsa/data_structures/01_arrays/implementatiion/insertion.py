
def insert_element(arr, index, element):

    if (index < 0) or (index > len(arr)):
        print('Invalid index')
        return
    
    # Increase the array size by one
    arr.append(None)

    # Shifting elements to the right to make space
    for i in range(len(arr)-1, index, -1):
        arr[i] = arr[i-1]
    
    arr[index] = element




# Example usage
arr = [10, 20, 30, 40]
insert_element(arr, 2, 25)
print(arr)

# Time Complexity: O(n), where n is the number of elements that need to be shifted. 
# Inserting at the end is O(1).