# A problem of Postfix expression

# Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN). 


def eval_rpn(tokens: list[str]) -> int:
    stack = []

    for token in tokens:
        if token in "+-*/":
            # Notice the order: b is popped first, then a.
            # first operand comes second (because it was pushed earlier).
            b = stack.pop()  # second operand
            a = stack.pop()  # first operand
            
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))  # Integer division
        else:
            stack.append(int(token))    # If the token is a number, push it onto the stack.

    # The final result will be the only element left in the stack.
    return stack[0]

# Example usage:
print(eval_rpn(["2", "1", "+", "3", "*"]))  # 9
print(eval_rpn(["4", "13", "5", "/", "+"])) # 6


