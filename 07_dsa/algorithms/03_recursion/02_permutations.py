# Generate all permutations of a given list or string.

def permutations(lst):
    if len(lst) == 0:
        return [[]]
    result = []
    for i in range(len(lst)):
        element = lst[i]
        remaining = lst[:i] + lst[i+1:]
        for perm in permutations(remaining):
            result.append([element] + perm)
    return result

# Example usage
print(permutations([1, 2, 3]))


