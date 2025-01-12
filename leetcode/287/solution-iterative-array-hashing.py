class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        curr = 0
        while nums[curr] != curr:
            nxt = nums[curr]
            nums[curr] = curr
            curr = nxt
        return curr