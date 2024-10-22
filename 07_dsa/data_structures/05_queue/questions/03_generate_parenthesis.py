# Given n pairs of parentheses, generate all combinations of well-formed parentheses.

def generate_parentheses(n: int) -> list[str]:
    def backtrack(s: str, left: int, right: int):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack("", 0, 0)
    return result

# Example usage:
print(generate_parentheses(3))
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
