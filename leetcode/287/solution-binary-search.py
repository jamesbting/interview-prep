class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1
        duplicate = 0
        while low <= high:
            mid = low + ((high - low) // 2)

            count = sum(n <= mid for n in nums)

            if count > mid:
                duplicate = mid
                high = mid - 1
            else:
                low = mid + 1
        return duplicate