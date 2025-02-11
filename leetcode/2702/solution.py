class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        low = 1
        high = max(nums) // y + 1
        while low < high:
            mid = (low + high) // 2
            if not self.is_valid(nums, mid, x, y):
                low = mid + 1
            else:
                high = mid
        return low

           
    def is_valid(self, nums, s, x, y):
        count = 0
        for n in nums:
            if n - (s * y) > 0: #if we can just ignore this value by decrementing other ones:
                count += ceil((n - (s * y)) / (x - y))
        return count <= s

   
        
# s: number of steps:
# (x * i + (s - i) * y) >= n
# xi + sy - yi >= n
# i(x -y) + sy >= n
# i >= (n - s * y) / (x - y)

