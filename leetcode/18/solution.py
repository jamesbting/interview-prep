class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #pick 2, and then the rest of the problem is just two-sum

        selections = set()

        for i in range(len(nums)):
            a = nums[i]
            for j in range(len(nums)):
                b = nums[j]
                if i == j
                    continue

                for c, d in self.twoSum(nums, target - a - b, {i, j}):
                    selections.add(tuple(sorted((a, b, c, d))))

        return [list(selection) for selection in selections]
                


    def twoSum(self, nums, target, toSkip):
        ans = []
        mp = set()
        for i in range(len(nums)):
            if i in toSkip:
                continue
            n = nums[i]
            if target - n in mp:
                ans.append((n, target - n))
            else:
                mp.add(n)
        return ans