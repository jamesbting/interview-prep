class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        buckets = [0 for _ in range(max_val - min_val + 1)]

        for n in nums:
            buckets[n - min_val] += 1

        for i in range(len(buckets) - 1, -1, -1):
            k -= buckets[i]
            if k <= 0:
                return i + min_val
        return -1

