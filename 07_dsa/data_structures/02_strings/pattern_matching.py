# Brute Force Method:
# Check every possible starting point in the string text for the pattern pat.
# Compare the substring of text starting from that point with pat.

def brute_force_pattern_matching(text, pat):
    n = len(text)
    m = len(pat)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pat[j]:
            j += 1
        if j == m:
            return i  # Pattern found at index i
    return -1  # Pattern not found


###################################################################

# Optimized Approach: KMP Algorithm (Knuth-Morris-Pratt):
# Preprocess the pattern to create a "longest prefix which is also suffix" (LPS) array.
# Use this LPS array to skip unnecessary comparisons.


def kmp_pattern_matching(text, pat):
    def compute_lps(pat):
        m = len(pat)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    n = len(text)
    m = len(pat)
    lps = compute_lps(pat)
    i = 0
    j = 0
    while i < n:
        if pat[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j  # Pattern found at index i - j
        elif i < n and pat[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1  # Pattern not found
