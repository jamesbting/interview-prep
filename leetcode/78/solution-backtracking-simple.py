class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        ## generate the subsets
        self.generate(nums, [])
        return self.ans

    def generate(self, nums, curr):
        self.ans.append(curr)
        for i in range(len(nums)):
            self.generate(nums[i + 1:], curr + [nums[i]])
