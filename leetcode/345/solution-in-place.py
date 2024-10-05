class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            if self.isVowel(s[left]) and self.isVowel(s[right]):
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
            else:
                if not self.isVowel(s[left]):
                    left += 1
                if not self.isVowel(s[right]):
                    right -= 1
        return "".join(s)
                
    
    def isVowel(self, c: str) -> bool:
        return c in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}