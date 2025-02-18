class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_0, next_2 = 0, len(nums) - 1
	
        for i in range(len(nums)):
        
            while next_2 > 0 and nums[next_2] == 2:
                next_2 -= 1
            
            while next_0 < len(nums) and nums[next_0] == 0:
                next_0 += 1
        
            if nums[i] == 0 and i > next_0:
                self.swap(nums, i, next_0)
            
            elif nums[i] == 2 and i < next_2:
                self.swap(nums, i, next_2)
      
      
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp