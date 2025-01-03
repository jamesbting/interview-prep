class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = right - (right - left) // 2
            if (nums[mid] - nums[0] - mid) < k:
                ## right half
                left = mid
            else:
                ## left half
                right = mid - 1

        return nums[0] + left + k
