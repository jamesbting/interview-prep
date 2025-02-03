class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_count = {}
        sum_count[0] = 1
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            if prefix_sum - k in sum_count:
                count += sum_count[prefix_sum - k]
            sum_count[prefix_sum] = sum_count[prefix_sum] + 1 if prefix_sum in sum_count else 1

        return count