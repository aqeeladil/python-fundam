
# Generate all subsets of a given list.

def subsets(lst):
    if not lst:
        return [[]]
    first, rest = lst[0], lst[1:]
    with_first = subsets(rest)
    with_first = [[first] + subset for subset in with_first]
    without_first = subsets(rest)
    return with_first + without_first

# Example usage
print(subsets([1, 2, 3]))


