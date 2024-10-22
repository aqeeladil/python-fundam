
# Infix to Postfix Conversion

'''
To convert infix expression to postfix expression, use the stack data structure. Scan the 
infix expression from left to right. Whenever we get an operand, add it to the postfix 
expression and if we get an operator or parenthesis add it to the stack by maintaining 
their precedence.
'''

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = []   # Stack to hold operators
    postfix = []   # List for output expression

    for char in expression:
        # If the character is an operand, add it to output
        if char.isalnum():
            postfix.append(char)

        # If the character is '(', push it to the stack
        elif char == '(':
            stack.append(char)

         # If the character is ')', pop until '(' is found
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '('

         # An operator is encountered
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(char)
    
    # Pop all the operators from the stack
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)

# Usage Example
infix_expression = "A+B*(C^D-E)"
postfix_expression = infix_to_postfix(infix_expression)
print(postfix_expression)  # Output: "ABCD^E-*+"
