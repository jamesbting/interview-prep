class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for d in text2] for c in text1]
        #dp[i][j] = longest commomn subsequence of text1[0..i] text2[0...j]
        
        dp[0][0] = 1 if text1[0] == text2[0] else 0

        #populate dp[i][0]
        for i in range(1, len(text1)):
            dp[i][0] = 1 if text1[i] == text2[0] else dp[i - 1][0]

        #populate dp[0][j]
        for j in range(1, len(text2)):
            dp[0][j] = 1 if text1[0] == text2[j] else dp[0][j - 1]

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                
                dp[i][j] = dp[i - 1][j - 1] + 1 if text1[i] == text2[j] else max(dp[i - 1][j], dp[i][j - 1])


        return dp[len(text1) - 1][len(text2) - 1]

