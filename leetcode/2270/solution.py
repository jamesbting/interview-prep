class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        leftSum, rightSum = 0, sum(nums)
        
        ans = 0
        for i in range(n - 1):
            leftSum += nums[i]
            rightSum -= nums[i]

            if leftSum >= rightSum:
                ans += 1
        return ans

