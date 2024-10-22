# Design a stack that supports push, pop, top, and retrieving the minimum 
# element in constant time.


class MinStack:
    def __init__(self):
        self.stack = []   # Main stack to store the elements
        self.min_stack = []    # Auxiliary stack to store the minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:  # min_stack[-1] -> top element
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def get_min(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return None

# Example usage:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min())  # -3
min_stack.pop()
print(min_stack.top())      # 0
print(min_stack.get_min())  # -2


