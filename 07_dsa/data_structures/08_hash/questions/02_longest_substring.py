

# Longest Substring Without Repeating Characters:

# Problem: Find the length of the longest substring without repeating characters in a string.

# Solution: Use a hash map to store the last index of each character and adjust the start 
# pointer of the substring accordingly.

def length_of_longest_substring(s):
    hash_map = {}
    max_length = start = 0
    for i, char in enumerate(s):
        if char in hash_map and hash_map[char] >= start:
            start = hash_map[char] + 1
        max_length = max(max_length, i - start + 1)
        hash_map[char] = i
    return max_length

# Usage
print(length_of_longest_substring("abcabcbb"))  # Output: 3
