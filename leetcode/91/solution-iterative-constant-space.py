class Solution:
    def numDecodings(self, s: str) -> int:        
        dp_i_2 = 1
        dp_i_1 = 1 if s[0] != '0' else 0

        for i in range(2, len(s) + 1):
            dp_i = 0
            if s[i - 1] != "0":
                dp_i += dp_i_1

            if 10 <= int(s[i-2:i]) and int(s[i-2:i]) <= 26:
                dp_i += dp_i_2

            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i_1