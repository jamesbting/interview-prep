class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        dp = [0 for _ in range(n)]
        dp[0] = values[0]

        best_score = 0

        for i in range(1, n):
            fixed = values[i] - i

            best_score = max(best_score, dp[i - 1] + fixed)

            dp[i] = max(dp[i - 1], values[i] + i)
        return best_score