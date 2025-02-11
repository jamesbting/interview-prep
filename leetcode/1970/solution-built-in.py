class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            if len(part) > len(s) or part not in s:
                break
            s = s.replace(part, '', 1)
        return s