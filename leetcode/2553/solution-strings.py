class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        chars = list("".join([str(n) for n in nums]))
        return [int(c) for c in chars]