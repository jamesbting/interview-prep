class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        ans = nums[0]

        for n in nums[1:]:
            temp_max = max_so_far
            max_so_far = max(n, max_so_far * n, min_so_far * n)
            min_so_far = min(n, min_so_far * n, temp_max * n)

            ans = max(ans, max_so_far)

        return ans
