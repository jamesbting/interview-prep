class NumberContainers:

    def __init__(self):
        self.nums = {}
        self.indexes = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.nums[index] = number
        heapq.heappush(self.indexes[number], index)

    def find(self, number: int) -> int:
        if number not in self.indexes or len(self.indexes[number]) < 1:
            return -1

        while self.indexes[number]:
            index = self.indexes[number][0]
            if number == self.nums[index]:
                return index
            heapq.heappop(self.indexes[number])

        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)