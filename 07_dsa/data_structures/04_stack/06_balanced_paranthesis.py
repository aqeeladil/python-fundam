# Given a string containing just the characters '(', ')', '{', '}', '[', and ']', 
# determine if the input string is valid. An input string is valid if the brackets are 
# closed in the correct order.


def is_valid_parentheses(s: str) -> bool:
    map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        # if it is an opening bracket
        if char in map.values():
            stack.append(char)

        # if it is a closing bracket
        elif char in map.keys():
            # Check if the stack is empty before popping
            if not stack or stack.pop() != map[char]:
                return False

        # In case of any invalid character (not a bracket)
        else:
            return False

    # If stack is empty, all opened brackets are closed properly
    return not stack

# Example usage:
print(is_valid_parentheses("()"))        # True
print(is_valid_parentheses("()[]{}"))    # True
print(is_valid_parentheses("(]"))        # False
print(is_valid_parentheses("([)]"))      # False
print(is_valid_parentheses("{[]}"))      # True
