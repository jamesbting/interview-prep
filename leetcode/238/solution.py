class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes, suffixes = [], []
        prefix, suffix = 1, 1
        for i in range(len(nums)):
            prefix *= nums[i]
            prefixes.append(prefix)
            suffix *= nums[len(nums) - 1 - i]
            suffixes.append(suffix)

        suffixes = suffixes[::-1]
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                ans[0] = suffixes[1]
            elif i == len(nums) - 1:
                ans[len(nums) - 1] = prefixes[len(nums) - 2]
            else:
                ans[i] = prefixes[i - 1] * suffixes[i + 1]
        return ans