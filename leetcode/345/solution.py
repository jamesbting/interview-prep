class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        queue = []

        for c in s:
            if self.isVowel(c):
                stack.insert(0, c)
            else:
                queue.append(c)

        ans = ''
        for c in s:
            if self.isVowel(c):
                ans = ans + stack.pop(0)
            else:
                ans = ans + queue.pop(0)
        return ans


    def isVowel(self, c: str) -> bool:
        return c in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}