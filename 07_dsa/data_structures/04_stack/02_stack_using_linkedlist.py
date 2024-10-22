
# Stack Implementation Using Linked Lists
# The top of the stack is represented by the head of the linked list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")
        value = self.head.value
        self.head = self.head.next
        return value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.head.value

# Usage Example
stack = StackLinkedList()
stack.push(10)
stack.push(20)
print(stack.peek())  # Output: 20
print(stack.pop())   # Output: 20
print(stack.is_empty())  # Output: False



## Advantages:
# Dynamic size; no limit on the number of elements.
# Efficient use of memory, no wasted space.

## Disadvantages:
# Extra memory is required for pointers in each node.
# Operations can be slightly slower due to pointer manipulation.
