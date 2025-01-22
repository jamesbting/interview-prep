from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.deque = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        if self.size == len(self.deque):
            self.sum -= self.deque.popleft()
        
        self.deque.append(val)
        self.sum += val
        
        return self.sum / len(self.deque)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)