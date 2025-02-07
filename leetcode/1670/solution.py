from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.front = deque()
        self.back = deque()
        

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        while len(self.front) - len(self.back) >= 2:
            self.back.appendleft(self.front.pop())

    def pushMiddle(self, val: int) -> None:
        if len(self.front) == len(self.back):
            self.front.append(val)
        else:
            self.back.appendleft(self.front.pop())
            self.front.append(val)

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        while len(self.front) < len(self.back):
            self.front.append(self.back.popleft())
        

    def popFront(self) -> int:
        if len(self.front) == 0 and len(self.back) == 0:
            return -1
        ans = self.front.popleft()
        while len(self.front) < len(self.back):
            self.front.append(self.back.popleft())
        return ans

    def popMiddle(self) -> int:
        if len(self.front) == 0 and len(self.back) == 0:
            return -1
        ans = self.front.pop()
        if len(self.front) < len(self.back):
            self.front.append(self.back.popleft())
        return ans
        

        
    def popBack(self) -> int:
        if len(self.front) == 0 and len(self.back) == 0:
            return -1
        if len(self.back) == 0:
            return self.front.pop()

        ans = self.back.pop()

        while len(self.front) - len(self.back) >= 2:
            self.back.appendleft(self.front.pop())

        return ans

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()


