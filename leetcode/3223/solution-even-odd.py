class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) < 3:
            return len(s)

        counts = [0 for _ in range(26)]
        for c in s:
            counts[ord(c) - ord('a')] += 1

        ans = 0
        for count in counts:
            if count == 0:
                continue
            elif count % 2 == 0:
                ans += 2
            else:
                ans += 1
        return ans