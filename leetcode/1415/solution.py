class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.count = 0
        self.chars = ['a', 'b', 'c']
        return self.generate(n, k, "")
    
    def generate(self, n, k, curr):
        if n == len(curr):
            if self.count == k - 1:
                return curr
            else:
                self.count += 1
            return ""

        for c in self.chars:
            if len(curr) > 0 and curr[-1] == c:
                continue
            temp = self.generate(n, k, curr + c)
            if temp:
                return temp
        return ""

        