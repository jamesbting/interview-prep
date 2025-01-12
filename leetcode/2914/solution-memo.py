class Solution:
    @lru_cache(maxsize = None)
    def minChanges(self, s: str) -> int:
        if s == '11' or s == '00':
            return 0
        if s == '10' or s == '01':
            return 1

        if (len(s) // 2) % 2 == 0:
            s_1 = s[:len(s)//2]
            s_2 = s[len(s)//2:]
            return self.minChanges(s_1) + self.minChanges(s_2)
        if len(s) > 5:
            div2 = len(s)//2
            s_1 = s[:div2 - 1]
            s_2 = s[div2 - 1: div2 + 1]
            s_3 = s[div2 + 1:]
            return self.minChanges(s_1) + self.minChanges(s_2) + self.minChanges(s_3)