class Solution:
    @lru_cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.myPow(x, -n)

        temp = self.myPow(x, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return x * temp * temp
            
            
