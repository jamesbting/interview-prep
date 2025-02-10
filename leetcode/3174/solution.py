class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c.isdigit() and len(stack) > 0:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
    
       