class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = [0 for _ in w]
        prfx_sum = 0
        for i, n in enumerate(w):
            prfx_sum += n
            self.prefix_sum[i] = prfx_sum
        self.total = self.prefix_sum[-1]

    def pickIndex(self) -> int:
        target = self.total * random.random()

        lo = 0
        hi = len(self.prefix_sum)

        while lo < hi:
            mid = (lo + hi) // 2
            if target > self.prefix_sum[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()