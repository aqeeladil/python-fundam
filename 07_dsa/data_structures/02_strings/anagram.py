# Anagram is when two strings contain the same characters in the same frequency but arranged differently.

# Problem: Check if two strings are anagrams.

# Solution 1: Sorting
def are_anagrams(s1, s2):

    # if length of strings are different, they can't be anagrams
    if len(s1) != len(s2):
        return False

    # create two dictionaries to store character counts
    char_count1 = {}
    char_count2 = {}

    # count charcters in string 1
    for i in s1:
        char_count1[i] = char_count1.get(i, 0) + 1

    # count charcters in string 2
    for i in s1:
        char_count2[i] = char_count2.get(i, 0) + 1

    # compare both dictionaries
    return char_count1 == char_count2
        

# Example:
s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))  # True


############################################################

# Solution 2: Counting Characters using collections.counter function

from collections import Counter

def are_anagrams(s1, s2):

    # if length of strings are different, they can't be anagrams
    if len(s1) != len(s2):
        return False
    
    # Use Counter to count the frequency of characters in both strings
    return Counter(s1) == Counter(s2)

# Example:
s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))  # True


'''
Time: O(n), 
where n is the length of the strings (since counting characters takes linear time).

Space: O(1),
for the hash map, since the size of the alphabet (in case of English letters) is 
constant (26 characters).
'''
