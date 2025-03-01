class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        s1, s2 = 0, 0
        while s1 < len(word) and s2 < len(abbr):
            if abbr[s2].isdigit():
                fast_fwd = 0
                
                if abbr[s2] == '0':
                    return False

                while s2 < len(abbr) and abbr[s2].isdigit():
                    fast_fwd = 10 * fast_fwd + int(abbr[s2])
                    s2 += 1
                
                if s1 + fast_fwd > len(word):
                    return False
                s1 += fast_fwd
            elif abbr[s2] != word[s1]:
                return False
            else:
                s2 += 1
                s1 += 1
        return s1 == len(word) and s2 == len(abbr)