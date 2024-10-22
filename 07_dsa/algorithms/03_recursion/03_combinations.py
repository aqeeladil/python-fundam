# Generate all combinations of a given size from a list or string.


def combinations(lst, size):
    if size == 0:
        return [[]]
    if not lst:
        return []
    first, rest = lst[0], lst[1:]
    with_first = combinations(rest, size-1)
    with_first = [[first] + comb for comb in with_first]
    without_first = combinations(rest, size)
    return with_first + without_first

# Example usage
print(combinations([1, 2, 3], 2))


