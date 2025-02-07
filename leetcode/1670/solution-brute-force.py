class FrontMiddleBackQueue:

    def __init__(self):
        self.q = []
        

    def pushFront(self, val: int) -> None:
        self.q.insert(0, val)    

    def pushMiddle(self, val: int) -> None:
        self.q.insert(len(self.q) // 2, val)     

    def pushBack(self, val: int) -> None:
        self.q.append(val)
        

    def popFront(self) -> int:
        if len(self.q) == 0:
            return -1 
        return self.q.pop(0)

    def popMiddle(self) -> int:
        if len(self.q) == 0:
            return -1 
        return self.q.pop(len(self.q) // 2 if len(self.q) % 2 == 1 else len(self.q) // 2 - 1)


    def popBack(self) -> int:
        if len(self.q) == 0:
            return -1 
        return self.q.pop()
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()