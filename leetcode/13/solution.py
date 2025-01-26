class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            'I':1,
            'V': 5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }

        ans = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and table[s[i]] < + table[s[i + 1]]:
                ans += table[s[i + 1]] - table[s[i]]
                i += 1
            else:
                ans += table[s[i]]
            i += 1
        return ans