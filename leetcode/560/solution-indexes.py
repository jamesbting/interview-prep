class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        sums = [0 for _ in range(n + 1)]
        sums[0] = 0

        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        count = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if sums[j] - sums[i] == k:
                    count += 1
        return count