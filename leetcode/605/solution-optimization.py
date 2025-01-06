class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i, pot in enumerate(flowerbed):
            prevPotOccupied = True if i > 0 and flowerbed[i-1] == 1 else False
            nextPotOccupied = True if i < len(flowerbed) - 1 and flowerbed[i+1] == 1 else False  

            if not prevPotOccupied and not nextPotOccupied and pot == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return n <= 0