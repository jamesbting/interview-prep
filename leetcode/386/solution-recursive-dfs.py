class Solution:
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        for i in range(1, 10):
            if i <= n:
                ans.append(i)
                self.generateNumbers(i, n, ans)
        return ans

    def generateNumbers(self, n, max, ans):
        if n > max:
            return

        for i in range(0, 10):
            if n * 10 + i <= max:
                ans.append(n * 10 + i)
                self.generateNumbers(n * 10 + i, max, ans)
            