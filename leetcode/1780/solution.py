class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 2:
            return False

        while n > 0:
            if n % 3 == 2:
                return False
            n = n // 3
        return True