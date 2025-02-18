from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0 : -1}
        count = 0
        maxx = 0
        for i in range(len(nums)):
            count += (1 if nums[i] == 1 else -1)

            if count in mp:
                maxx = max(maxx, i - mp[count])
            else:
                mp[count] = i
        return maxx
