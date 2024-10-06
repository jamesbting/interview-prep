class Solution:
    def numTilings(self, n: int) -> int:
        return (self.numTilingsRec(n, [-1 for i in range(0, n + 3)]))
        
    def numTilingsRec(self, n: int, dp: List[int]) -> int:
        if n < 3:
            return n
        if n == 3:
            return 5
        if dp[n] != -1:
            return dp[n]

        dp[n] = (self.numTilingsRec(n - 1, dp) * 2) + self.numTilingsRec(n - 3, dp)
        return dp[n] % (10 ** 9 + 7) 