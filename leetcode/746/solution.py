class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [1000 for i in range(0, len(cost) + 1)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        i = 2
        while i < len(cost):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
            i += 1

        return  min(dp[i - 1], dp[i - 2])
