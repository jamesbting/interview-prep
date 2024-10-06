class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sumLeft = [0 for i in nums]
        sumRight = [0 for i in nums]
        i = 0
        while i < n:
            if i == 0:
                sumLeft[i] = nums[i]
            else:
                sumLeft[i] = sumLeft[i - 1] + nums[i]
            i += 1

        i = n - 1

        while i >= 0:
            if i == n - 1:
                sumRight[i] = nums[i]
            else:
                sumRight[i] = sumRight[i + 1] + nums[i]
            i -= 1

        print(sumLeft)
        print(sumRight)
        i = 0
        while i < n:
            if sumLeft[i] == sumRight[i]:
                return i
            i += 1
        return -1
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sumLeft = [0 for i in nums]
        sumRight = [0 for i in nums]
        i = 0
        while i < n:
            if i == 0:
                sumLeft[i] = nums[i]
            else:
                sumLeft[i] = sumLeft[i - 1] + nums[i]
            i += 1

        i = n - 1

        while i >= 0:
            if i == n - 1:
                sumRight[i] = nums[i]
            else:
                sumRight[i] = sumRight[i + 1] + nums[i]
            i -= 1

        print(sumLeft)
        print(sumRight)
        i = 0
        while i < n:
            if sumLeft[i] == sumRight[i]:
                return i
            i += 1
        return -1
