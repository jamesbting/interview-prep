class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right  = 0, k
        roll_sum = sum(nums[0:k])
        ans = roll_sum
        while right < len(nums):
            roll_sum = roll_sum - nums[left] + nums[right]
            ans = max(ans, roll_sum)
            right += 1
            left += 1

        return ans / k