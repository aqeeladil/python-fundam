# Check if a string has all unique characters:

# Example: "abcde" → True, "hello" → False

# Appoarch-1
# Time: O(n) 
# Space: O(n)
def has_unique_characters(s):
    if len(s) > 128:  # Since ASCII has 128 unique characters
        return False
    
    char_set = [False] * 128
    for char in s:
        index = ord(char)  # Get ASCII value
        if char_set[index]:
            return False
        char_set[index] = True
    return True

######################################################

# Appoarch-2 (using sets)
# Time: O(nlogn)  
# Space: O(n)
def is_unique(s):
    return len(set(s)) == len(s)

####################################################

# Appoarch-3 (using sorting function)
# Time: O(nlogn)  
# Space: O(1)
def uniqueCharacters(st):
    # Using sorting
    st = sorted(st)
 
    for i in range(len(st)-1):
 
        if (st[i] == st[i + 1]) :
            return False   
    return True

###################################################

# Appoarch-4 (brute force)
# Time: O(n^2) 
# Space: O(1)
def uniqueCharacters2(str):
    
    for i in range(len(str)):
        for j in range(i + 1,len(str)): 
            if(str[i] == str[j]):
                return False
 
    return True
