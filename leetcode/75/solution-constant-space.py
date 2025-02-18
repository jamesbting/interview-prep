class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_0, next_2 = 0, len(nums) - 1
	
        i = 0
        while i <= next_2:
    
            if nums[i] == 0:
                nums[i], nums[next_0] = nums[next_0], nums[i]
                next_0 += 1
                i += 1
            
            elif nums[i] == 2:
                nums[i], nums[next_2] = nums[next_2], nums[i]
                next_2 -= 1
            else:
                i += 1
