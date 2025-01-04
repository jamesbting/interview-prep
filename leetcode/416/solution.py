class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False

        return self.dfs(tuple(nums), len(nums) - 1, target // 2)

    @lru_cache(maxsize=None)
    def dfs(self, nums, n, target):
        if target == 0:
            return True
        if n == 0 or target < 0:
            return False
        return self.dfs(nums, n - 1, target - nums[n - 1]) or self.dfs(nums, n - 1, target)