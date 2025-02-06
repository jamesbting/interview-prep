class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        count = defaultdict(int)
        n = len(nums)
        for i in range(n):
            a = nums[i]
            for j in range(i + 1, n):
                b = nums[j]
                count[a * b] += 1

        for c in count.values():
            pairs = ((c - 1) * c) // 2
            ans += 8 * pairs
        return ans