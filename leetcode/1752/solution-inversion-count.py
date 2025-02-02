class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        inversions = 0

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                inversions += 1

        if nums[n - 1] > nums[0]:
            inversions += 1

        return inversions <= 1
        