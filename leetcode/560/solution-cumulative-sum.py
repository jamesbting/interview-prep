class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            prefix_sum = 0
            for j in range(i, len(nums)):
                prefix_sum += nums[j]
                if prefix_sum == k:
                    count += 1
                    break
        return count