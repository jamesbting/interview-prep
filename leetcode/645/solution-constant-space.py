class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        double, missing = -1, 1

        for n in nums:
            if nums[abs(n) - 1] < 0:
                double = abs(n)
            else:
                nums[abs(n) - 1] *= -1

        for i in range(1, len(nums)):
            if nums[i] > 0:
                missing = i + 1

        return [double, missing]
        
        