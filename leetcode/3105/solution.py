class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        #longest increase
        ans = 0
        for left in range(len(nums)):
            right = left
            while right < len(nums) - 1 and nums[right] < nums[right + 1]:
                right += 1
            ans = max(ans, right - left + 1)

        
        #longest decrease
        for left in range(len(nums)):
            right = left
            while right < len(nums) - 1 and nums[right] > nums[right + 1]:
                right += 1
            ans = max(ans, right - left + 1)
        return ans