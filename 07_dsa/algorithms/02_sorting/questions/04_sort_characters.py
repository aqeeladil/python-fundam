# Sort Characters By Frequency
# Given a string, sort it in decreasing order based on the frequency of characters.

from collections import Counter

def frequency_sort(s):
    freq_map = Counter(s)
    sorted_chars = sorted(freq_map.items(), key=lambda x: -x[1])
    result = ''.join([char * freq for char, freq in sorted_chars])
    return result

# Example usage:
s = "tree"
print(frequency_sort(s))  # Output: "eert"


