class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        pair = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            diff = nums[i] - i
            ans += i - pair[diff]
            pair[diff] += 1
        

        return ans


