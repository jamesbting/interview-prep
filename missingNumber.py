# https: // leetcode.com/problems/missing-number/
# O(nlogn) sort the list and look for a difference of 2, and once you find
# it then return the element preceding the skip of 2 plus one

# O(n) use the arithmetic sum formula n(n+1)/2 and sum all the elements, and track if you saw a zero ->
# if you didnt find a zero, return zero, else return the difference between the actual sum and the arithmetic sum
class Solution:
    def missingNumberSlow(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 1:
                return 0
            else:
                return 1
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(len(nums)-1):
            if(nums[i + 1] - nums[i] == 2):
                return nums[i] + 1

        return nums[len(nums) - 1] + 1

    def missingNumberFast(self, nums: List[int]) -> int:
        sum = 0
        for n in nums:
            sum += n
        arithmeticSum = (len(nums) * (len(nums) + 1)) / 2
        return int(arithmeticSum - sum)
