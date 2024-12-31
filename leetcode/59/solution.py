class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_so_far = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            sum_so_far = max(nums[i], sum_so_far + nums[i])
            ans = max(sum_so_far, ans)
        return ans
