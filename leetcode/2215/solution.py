class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        one_digits, two_digits = set(nums1), set(nums2)
        return [one_digits.difference(two_digits), two_digits.difference(one_digits)]
