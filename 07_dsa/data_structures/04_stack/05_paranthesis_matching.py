

## Parentheses Matching
'''Parentheses matching is the process of checking whether every opening parenthesis 
((, {, [) in an expression has a corresponding closing parenthesis (), }, ]) and 
that the pairs are properly nested.
'''


def is_parentheses_balanced(expression):
    stack = []
    # Dictionary to hold matching pairs
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in mapping.values():  # if it is an opening bracket
            stack.append(char)
        elif char in mapping:  #  # if it is a closing bracket
            if stack and stack[-1] == mapping[char]:  # if top most element in stack matches its opening bracket value
                stack.pop()
            else:
                return False
     
    # If the stack is empty, all opening brackets had matching closing brackets
    return stack == []
       

# Usage Example
expression = "{[()]}"
print(is_parentheses_balanced(expression))  # Output: True

expression = "{[(])}"
print(is_parentheses_balanced(expression))  # Output: False
