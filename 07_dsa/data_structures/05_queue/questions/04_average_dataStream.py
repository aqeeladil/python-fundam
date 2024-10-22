# Implement a moving average from a data stream. The class MovingAverage should have 
# methods to add a value to the stream and return the moving average of the last k values.

from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            self.total -= self.window.popleft()
        self.window.append(val)
        self.total += val
        return self.total / len(self.window)

# Example usage:
moving_average = MovingAverage(3)
print(moving_average.next(1))  # 1.0
print(moving_average.next(10)) # 5.5
print(moving_average.next(3))  # 4.66667
print(moving_average.next(5))  # 6.0
