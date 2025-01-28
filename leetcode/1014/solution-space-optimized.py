class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        # dp = [0 for _ in range(n)]
        best_left = values[0]

        best_score = 0

        for i in range(1, n):
            fixed = values[i] - i

            best_score = max(best_score, best_left + fixed)

            best_left = max(best_left, values[i] + i)
        return best_score