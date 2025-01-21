class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #find the first descending nodes
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
                i-= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i + 1, len(nums) - 1)

    def reverse(self, nums, left, right):
        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
            