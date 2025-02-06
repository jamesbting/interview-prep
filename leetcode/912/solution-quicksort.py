class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, l, r):
        if l >= r or l < 0:
            return

        p = self.partition(nums, l, r)
        self.quicksort(nums, l, p - 1)
        self.quicksort(nums, p + 1, r)

    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l
        for j in range(l, r):
            if nums[j] <= pivot:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
           
                i += 1

        temp = nums[i]
        nums[i] = nums[r]
        nums[r] = temp
        return i