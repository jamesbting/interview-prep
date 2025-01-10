class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashmap = [0] * len(nums)

        for n in nums:
            hashmap[n - 1] += 1

        return [i + 1 for i in range(0, len(hashmap)) if hashmap[i] == 2] + [i + 1 for i in range(0, len(hashmap)) if hashmap[i] == 0]
        