class Solution:
    def numDecodings(self, s: str) -> int:
        return self.solve(s, 0)


    @cache
    def solve(self, s, start):
        if start == len(s):
            return 1

        if s[start] == '0':
            return 0

        if start == len(s) - 1:
            return 1

        ans = self.solve(s, start + 1)
        if int(s[start: start + 2]) <= 26:
            ans += self.solve(s, start + 2)
        return ans
        