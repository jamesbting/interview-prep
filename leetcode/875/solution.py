class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high:
            mid = (high + low) // 2

            if not self.canFinish(piles, h, mid): 
                low = mid + 1
            else:
                high = mid - 1

        return low

            

    def canFinish(self, piles: List[int], h: int, k: int):
        for pile in piles:
            h -= ceil(pile / k)
        return h >= 0
