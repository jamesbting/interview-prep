class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            missed_in_gap = nums[i] - nums[i - 1] - 1

            if missed_in_gap >= k:
                return nums[i-1] + k
            k -= missed_in_gap
        return nums[len(nums) - 1] + k