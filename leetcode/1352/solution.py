class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]
        self.size = 0
        

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = [1]
            self.size = 0
        else:
            self.nums.append(self.nums[self.size] * num)
            self.size += 1
        

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        ## last k items would be products[num_items] // products[num_items - k]
        return self.nums[self.size] // self.nums[self.size - k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)