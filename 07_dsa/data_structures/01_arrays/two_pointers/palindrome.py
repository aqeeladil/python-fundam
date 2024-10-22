# Given a string, determine if it is a palindrome (ignoring spaces, punctuation, and case).


def is_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Check for equality ignoring case
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# Example usage
s = "A man, a plan, a canal: Panama"
result = is_palindrome(s)
print(result)  # Output: True



# Time Complexity: O(n), where n is the length of the string.

