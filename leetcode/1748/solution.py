class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = [0 for _ in range(max(nums) + 1)]

        for n in nums:
            count[n] += 1
        
        ans = 0
        for i in range(len(count)):
            if count[i] == 1:
                ans += i
        return ans