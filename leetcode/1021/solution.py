class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        primative = "("
        balance = 1
        for i in range(1, len(s)):
            c = s[i]
            balance += 1 if c == '(' else -1
            primative += c
            
            #found a primative
            if balance == 0:
                ans += primative[1:len(primative)-1]
                primative = ""
        return ans