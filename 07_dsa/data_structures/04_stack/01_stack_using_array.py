
# Using arrays, the stack is represented as a fixed-size array where 
# elements are added or removed from the top.


class StackArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capacity - 1
    
    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack Overflow")
        self.top += 1
        self.stack[self.top] = value
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")
        value = self.stack[self.top]
        self.top -= 1
        return value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.stack[self.top]

# Usage Example
stack = StackArray(5)
stack.push(10)
stack.push(20)
print(stack.peek())  # Output: 20
print(stack.pop())   # Output: 20
print(stack.is_empty())  # Output: False



## Advantages:
# Fast access time (O(1) for push, pop, and peek operations).
# Simple to implement.

## Disadvantages:
# Fixed size; cannot dynamically resize.
# May lead to wasted space if the stack is not fully used.