class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        
        while i <= j:
            if s[i] != s[j]:
                return self.check_palindrome(s, i + 1, j) or self.check_palindrome(s, i, j - 1)
            i += 1
            j -= 1
        return True

                
    def check_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True