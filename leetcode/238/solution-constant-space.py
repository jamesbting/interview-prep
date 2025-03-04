class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for _ in range(n)]
        for i in range(1, n):
            ans[i] = nums[i - 1] * ans[i - 1]
            
        product = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= product
            product *= nums[i]

        return ans