class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.merge(nums1, nums2)

        if len(merged) % 2 == 1:
            return float(merged[len(merged) // 2])
        else:
            return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2

    def merge(self, nums1, nums2):
        ans = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        if i < len(nums1):
            ans.extend(nums1[i:])

        if j < len(nums2):
            ans.extend(nums2[j:])
        return ans