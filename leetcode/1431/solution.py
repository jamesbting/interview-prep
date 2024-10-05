class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = 0
        for candy in candies:
            maxCandies = max(maxCandies, candy)

        return [candy + extraCandies >= maxCandies for candy in candies]