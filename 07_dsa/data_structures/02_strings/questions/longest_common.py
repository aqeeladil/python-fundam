# Find the longest common prefix among an array of strings.
# Example: ["flower", "flow", "flight"] → "fl"


def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # "fl"



##############################################
# 2nd Approach

class Solution:
    def longestCommonPrefix(strs):

        res = ""
        strs = sorted(strs)
        st = strs[0]
        en = strs[-1]

        # Iterate over the characters of the first and last strings up to 
        # the length of the shorter string
        for i in range( min( len(st), len(en) )):
            if st[i] != en[i]:
                return res

            res += st[i]

        return res


        