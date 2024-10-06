class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        ans = []
        for spell in spells:
            ## find the smallest potion that succeeds using binary search
            nums = self.binarySearch(potions, (success + spell - 1) // spell, 0, len(potions) - 1)
            ans.append(len(potions) - nums)
        return ans

    def binarySearch(self, nums, item, low, high):
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] >= item:
                high = mid - 1
            else:
                low = mid + 1

        return low