class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word1_counts = {}
        min_universal_count = [0] * 26
        for b in words2:
            b_count = self.countLetters(b)
            min_universal_count = [max(min_universal_count[i], b_count[i]) for i in range(0, 26)]
            
        ans = []
        for a in words1:
            a_count = self.countLetters(a)
            t = sum([1 if a_count[i] >= min_universal_count[i] else 0 for i in range(0, 26)]) 
            if sum([1 if a_count[i] >= min_universal_count[i] else 0 for i in range(0, 26)]) == 26:
                ans.append(a)
        return ans

    def countLetters(self, word):
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        return count