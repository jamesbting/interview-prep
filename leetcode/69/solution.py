class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 2, x // 2
        while low < high:
            mid = low + ((high - low) / 2)
            squared = mid * mid
            if squared == x:
                return int(mid)
            elif squared > x: 
                high = mid - 1
            else:
                low = mid + 1
        return int(high)
        