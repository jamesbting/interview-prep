class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for query in queries:
            for word in dictionary:
                if self.areEqualAfter2Edits(query, word):
                    ans.append(query)
                    break
        return ans
        

    def areEqualAfter2Edits(self, s1, s2):
        diffCount = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffCount += 1
            if diffCount > 2:
                return False
        return diffCount <= 2