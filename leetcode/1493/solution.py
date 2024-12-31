class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right, numsZero = 0, 0, 0
        ans = 0
        while left < len(nums) and right < len(nums):
            if nums[right] == 0:
                numsZero += 1

            while numsZero > 1:
                if nums[left] == 0:
                    numsZero -= 1
                left += 1
            
            ans = max(ans, right - left)
            right += 1

            
        if left == 0 and right == len(nums):
            return len(nums) - 1
        return ans

