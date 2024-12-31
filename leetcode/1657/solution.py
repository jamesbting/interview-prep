class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): 
            return False

        i = 0
        count1 = {}
        count2 = {}
        while i < len(word1):
            c1 = word1[i]
            c2 = word2[i]
            count1[c1] = 1 if c1 not in count1 else count1[c1] + 1
            count2[c2] = 1 if c2 not in count2 else count2[c2] + 1
            i += 1
        
        return sorted(count1.values()) == sorted(count2.values()) and sorted(count1.keys()) == sorted(count2.keys())