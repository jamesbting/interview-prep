class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) < 3:
            return len(s)

        counts = [0 for _ in range(26)]

        hasMoreThan3 = False
        for c in s:
            counts[ord(c) - ord('a')] += 1
            if counts[ord(c) - ord('a')] >= 3:
                hasMoreThan3 = True

        while hasMoreThan3:
            hasMoreThan3AfterStep = False
            for i in range(26):
                count = counts[i]
                if count >= 3:
                    counts[i] -= 2
                    hasMoreThan3AfterStep = hasMoreThan3AfterStep or counts[i] >= 3
            hasMoreThan3 = hasMoreThan3AfterStep
        
        return sum(counts)