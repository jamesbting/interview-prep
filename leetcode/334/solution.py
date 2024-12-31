class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        first, second = math.inf, math.inf
        for n in nums:
            if n < first:
                first = n
            elif n > first and n < second:
                second = n
            elif n > second:
                return True

        return False