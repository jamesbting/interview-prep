class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self.solve(s, k, 0, len(s))

       

    def solve(self, s, k, start, end):
        if end < k:
            return 0
        map = {}
        for i in range(start, end):
            c = s[i]
            if c in map:
                map[c] += 1
            else:
                map[c] = 1
        max_count = 0
        for i in range(start, end):
            if map[s[i]] < k:
                midNext = i + 1
                while (midNext < end and map[s[midNext]] < k):
                     midNext += 1
                return max(
                    self.solve(s, k, start, i),
                    self.solve(s, k, midNext, end)
                )
        return end - start