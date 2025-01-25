from collections import deque
class Solution:
    
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)
        num_to_group = {}
        num_to_group[sorted_nums[0]] = 0
        group = 0

        group_to_nums = defaultdict(deque)
        group_to_nums[0].append(sorted_nums[0])
        for i in range(1, len(nums)):
            if abs(sorted_nums[i] - sorted_nums[i - 1]) > limit:
                group += 1

            num_to_group[sorted_nums[i]] = group
            group_to_nums[group].append(sorted_nums[i])

        for i in range(len(nums)):
            nums[i] = group_to_nums[num_to_group[nums[i]]].popleft()
        return nums