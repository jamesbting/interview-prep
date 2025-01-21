class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the pivot by doing binary search but comparing if the orders match
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        low = 0
        high = len(nums) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2
            if nums[-1] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        pivot = low

        def binarySearch(left_bound, right_bound):
            low = left_bound
            high = right_bound
            while low <= high:
                mid = (low + high) // 2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1

        left_ans = binarySearch(0, pivot - 1)
        if left_ans == -1:
            return binarySearch(pivot, len(nums) - 1)
        return left_ans