class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        groups = defaultdict(list)
        for n in nums:
            heapq.heappush(groups[self.sumOfDigits(n)], -n)

        ans = -1
        for heap in groups.values():
            if len(heap) >= 2:
                ans = max(ans, abs(heapq.heappop(heap) + heapq.heappop(heap)))
        return ans
            


    def sumOfDigits(self, n):
        ans = 0
        while n > 0:
            ans += n % 10
            n = n // 10
        return ans