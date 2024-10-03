class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr, last_digit = 0, 0
        while curr < len(nums):
            if(nums[curr] != 0):
                nums[last_digit] = nums[curr]
                last_digit += 1
            curr += 1          
            
        while last_digit < len(nums):
            nums[last_digit] = 0
            last_digit += 1