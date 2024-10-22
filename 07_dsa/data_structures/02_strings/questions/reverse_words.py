# Reverse Words in a String:

# Reverse the order of words in a given string.
# Example: "the sky is blue" → "blue is sky the

def reverse_words(s):

    words = s.split()
    reversed_words = reversed(words)

    return " ".join(reversed_words)
    

s = "the sky is blue"
print(reverse_words(s))  # "blue is sky the"

# 2nd Approach
def reverse_words2(s):
    s = s.strip()   # trim the string
    words = s.split()  # split by whitespace and filter out any empty parts
    reversed_words = words[::-1]  

    return ' '.join(reversed_words)


# Time O(n)
# Space O(n), for storing words in a list
