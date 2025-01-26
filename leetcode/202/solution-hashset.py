class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            nxt = self.getNext(n)
            if nxt in visited:
                return False
            visited.add(nxt)
            n = nxt
        return True

        
    def getNext(self, n):
        ans = 0
        while n > 0:
            digit = n % 10
            ans += digit * digit
            n = n // 10  
        return ans