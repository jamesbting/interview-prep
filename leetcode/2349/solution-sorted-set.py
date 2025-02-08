class NumberContainers:

    def __init__(self):
        self.nums = {}
        self.indexes = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.nums:
            old_value = self.nums[index]
            self.indexes[old_value].remove(index)
        self.nums[index] = number
        self.indexes[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.indexes or len(self.indexes[number]) < 1:
            return -1

        return self.indexes[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)