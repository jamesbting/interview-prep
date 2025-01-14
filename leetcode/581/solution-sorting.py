class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = nums[:]
        sorted_nums.sort()

        left, right = len(sorted_nums) - 1, 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                left = min(i, left)
                right = max(i, right)
            

        return right - left + 1 if right - left > 0 else 0