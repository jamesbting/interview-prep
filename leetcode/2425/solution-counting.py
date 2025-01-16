class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        max1 = max(nums1)
        max2 = max(nums2)

        limit = max(max1, max2)
        count = {}        
        for n1 in nums1:
            if n1 in count:
                count[n1] += len(nums2)
            else:
                count[n1] = len(nums2)
        
        for n2 in nums2:
            if n2 in count:
                count[n2] += len(nums1)
            else:
                count[n2] = len(nums1)
        

        ans = 0
        for i in count.keys():
            if count[i] % 2 == 1:
                ans ^= i
        return ans