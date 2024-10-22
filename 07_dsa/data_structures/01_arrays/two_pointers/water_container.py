# Container With Most Water
# You are given an array of non-negative integers where each element represents 
# the height of a vertical line. The task is to find two lines such that together 
# with the x-axis, they form a container that holds the most water.



def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate the area
        width = right - left
        water = min(height[left], height[right]) * width
        max_water = max(max_water, water)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

# Example usage
height = [1,8,6,2,5,4,8,3,7]
result = max_area(height)
print(result)  # Output: 49


# Time Complexity: O(n), where n is the length of the height array.