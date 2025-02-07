from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.front = deque()
        self.back = deque()
        
    def rebalance(self):
        if len(self.front) - 1 > len(self.back):
            self.back.appendleft(self.front.pop())
        
        if len(self.front) < len(self.back):
            self.front.append(self.back.popleft())


    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front) - 1 == len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)
        self.rebalance()

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self.rebalance()
        

    def popFront(self) -> int:
        if len(self.front) == 0:
            return -1
        ans = self.front.popleft()
        self.rebalance()
        return ans

    def popMiddle(self) -> int:
        if len(self.front) == 0 and len(self.back) == 0:
            return -1
        ans = self.front.pop()
        self.rebalance()
        return ans
        

        
    def popBack(self) -> int:
        if len(self.front) == 0 and len(self.back) == 0:
            return -1
        if len(self.back) == 0:
            return self.front.pop()

        ans = self.back.pop()
        self.rebalance()
        return ans

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()



