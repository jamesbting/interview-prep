class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        remaining, pot = n, 0
        while pot < len(flowerbed) and remaining > 0:
            empty_pot_before = flowerbed[pot - 1] == 0 if pot > 0 else True
            empty_pot_after = flowerbed[pot + 1] == 0 if pot < len(flowerbed) - 1 else True
            if empty_pot_before and empty_pot_after and flowerbed[pot] == 0:
                flowerbed[pot] = 1
                remaining -= 1
            pot += 1
        
        return remaining == 0
        

# remaining = 1
# pot = 2
# [1,0,1,0,1]