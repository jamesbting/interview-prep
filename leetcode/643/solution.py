class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        rolling_sum = 0
        left, right = 0, 0
        while right < len(nums):
            if right < k:
                rolling_sum += nums[right]
                right += 1
                max_sum = rolling_sum
            else: 
                rolling_sum = rolling_sum - nums[left] + nums[right]
                max_sum = max(max_sum, rolling_sum)
                left += 1
                right += 1
        return max_sum / k