class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""
        for i in range(len(nums)):
            s = nums[i]
            ans += '1' if s[i] == '0' else '0'
        return ans

