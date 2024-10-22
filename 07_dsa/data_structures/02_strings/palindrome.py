# Palindromes
# Palindrome is a string that reads the same forward and backward.

# Problem 1: Check if a string is a palindrome.
def is_palindrome(s):
    st = 0
    en = len(s) - 1

    while st < en:
        while st < en and not s[st].isalnum():
            st += 1
        while st < en and not s[en].isalnum():
            en -= 1

        if s[st].lower() != s[en].lower():
            return False
        st += 1
        en -= 1

    return True

# Example:
s = "madam"
print(is_palindrome(s))  # True



##########################################################

# Problem 2: Longest Palindromic Substring.
# Given a string, find the longest substring that is a palindrome.
# Expand Around Center Approach: 
# O(n²) time and O(1) space.

def longestPalindrome(self, s: str) -> str:
        
        # Handle empty string case
        if len(s) == 0:
            return ""
        
        res = ""   # longest palindrome found so far.
        max_len = 0   # length of the longest palindrome found.

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If the current palindrome is longer than the previously stored one (max_len), 
                # the substring is updated as the new longest palindrome.
                if (r - l + 1) > max_len:
                    res = s[l : r + 1]
                    max_len = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    res = s[l : r + 1]
                    max_len = r - l + 1
                l -= 1
                r += 1

        return res

# Example:
s = "babad"
print(longestPalindrome(s))  # "bab" or "aba"



    