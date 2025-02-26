class SparseVector:
    def __init__(self, nums: List[int]):
        self.v = []
        for i, n in enumerate(nums):
            if n != 0:
                self.v.append((i, n))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        i, j = 0, 0
        while i < len(self.v) and j < len(vec.v):
            if self.v[i][0] == vec.v[j][0]:
                ans += self.v[i][1] * vec.v[j][1]
                i += 1
                j += 1
            elif self.v[i][0] < vec.v[j][0]:
                i += 1
            else:
                j += 1

        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)