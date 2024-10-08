class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if mid > 0 and nums[mid - 1] > nums[mid]:
                high = mid - 1
            elif mid < n - 1 and nums[mid + 1] > nums[mid]:
                low = mid + 1
            else:
                return mid
