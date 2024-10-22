

# Group Anagrams:

# Problem: Given an array of strings, group the anagrams together.

# Solution: Use a hash map where the key is the sorted version of the string and the value 
# is the list of anagrams.

from collections import defaultdict

def group_anagrams(strs):
    hash_map = defaultdict(list)
    for s in strs:
        sorted_s = ''.join(sorted(s))
        hash_map[sorted_s].append(s)
    return list(hash_map.values())

# Usage
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
