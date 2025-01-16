class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        xor1 = 0
        if n % 2 == 1:
            for i in nums1:
                xor1 ^= i

        
        xor2 = 0
        if m % 2 == 1:
            for i in nums2:
                xor2 ^= i

        return xor1 ^ xor2