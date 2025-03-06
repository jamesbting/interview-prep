class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = [0 for _ in range(26)]

        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        ans = ""
        for c in order:
            for _ in range(counts[ord(c) - ord('a')]):
                ans += c
            counts[ord(c) - ord('a')] = 0
        
        for c in s:
            if counts[ord(c) - ord('a')] > 0:
                for _ in range(counts[ord(c) - ord('a')]):
                    ans += c
                counts[ord(c) - ord('a')] = 0
        return ans