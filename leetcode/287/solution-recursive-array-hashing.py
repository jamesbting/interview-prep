class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.store(nums, 0)

    def store(self, nums, curr):
        if nums[curr] == curr:
            return curr
        nxt = nums[curr]
        nums[curr] = curr
        return self.store(nums, nxt)
        

