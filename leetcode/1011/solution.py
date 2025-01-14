class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)

        while low < high:
            mid = (high + low) // 2

            canHold = self.canShipAll(weights, days, mid)

            if canHold:
                high = mid
            else:
                low = mid + 1
        return low


    def canShipAll(self, weights, days, capacity):
        daysNeeded = 1
        currCapacity = 0
        for weight in weights:
            currCapacity += weight
            if currCapacity > capacity:
                daysNeeded += 1
                currCapacity = weight
        
        return daysNeeded <= days