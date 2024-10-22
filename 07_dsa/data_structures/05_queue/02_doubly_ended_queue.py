# Deque (Double-Ended Queue)
# A Deque allows insertion and deletion of elements from both ends (front and rear).

# Key Operations:
'''
Append (Insert at rear)
Append Left (Insert at front)
Pop (Remove from rear)
Pop Left (Remove from front)
Peek (Get element at the front)
Peek Rear (Get element at the rear)
Implementation using Python's collections.deque:
'''


from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()

    def append(self, item):
        self.deque.append(item)

    def append_left(self, item):
        self.deque.appendleft(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.deque.pop()

    def pop_left(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.deque.popleft()

    def peek(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.deque[0]

    def peek_rear(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.deque[-1]

    def is_empty(self):
        return len(self.deque) == 0
