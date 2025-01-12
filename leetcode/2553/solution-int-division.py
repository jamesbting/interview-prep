class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            stack = []
            while n != 0:
                stack.append(n % 10)
                n = n // 10
            
            stack.reverse()
            res.extend(stack)

        return res
