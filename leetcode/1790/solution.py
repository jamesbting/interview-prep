class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        num_diffs = 0
        first, second = -1, -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_diffs += 1
                if num_diffs > 2:
                    return False
                elif num_diffs == 1:
                    first = i
                else:
                    second = i

        return s1[first] == s2[second] and s1[second] == s2[first]
            