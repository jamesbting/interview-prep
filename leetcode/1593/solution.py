class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.max_count = 0
        self.backtrack(s, 0, 0, set())
        return self.max_count

    def backtrack(self, s, start, count, seen):
        if count + (len(s) - start) <= self.max_count:
            return

        if start == len(s):
            self.max_count = max(self.max_count, count)
            return

        max_count = 0

        for i in range(start + 1, len(s) + 1):
            substring = s[start:i]
            if substring not in seen:
                seen.add(substring)
                self.backtrack(s, i, count + 1, seen)
                seen.remove(substring)
