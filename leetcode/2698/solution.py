class Solution:
    def punishmentNumber(self, n: int) -> int:
        punishmentNumber = 0
        for i in range(1, n + 1):
            if self.partition(i * i, i):
                punishmentNumber += i * i
        return punishmentNumber
        
    @lru_cache
    def partition(self, n, target):
        if target < 0 or n < target:
            return False

        if n == target:
            return True

        return self.partition(n // 10, target - n % 10) or self.partition(n // 100, target - n % 100) or self.partition(n // 1000, target - n % 1000)
