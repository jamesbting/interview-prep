class Solution:
    def feasible(self, nums, d, threshold):
        return sum([ceil(n / d) for n in nums]) <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        while(low < high - 1):
            mid = (low + high) // 2
            
            if self.feasible(nums, mid, threshold):
                high = mid
            else:
                low = mid + 1

        return low if self.feasible(nums, low, threshold) else high