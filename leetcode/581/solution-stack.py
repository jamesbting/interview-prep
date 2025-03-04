class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        left = len(nums)
        for i in range(len(nums)):
            while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)

        stack = []
        right = 0
        for i in range(len(nums) - 1, -1, -1):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)

        return right - left + 1 if right - left > 0 else 0