class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        sorted_nums = sorted(nums)
        for x in range(n):
            is_sorted = True
            for i in range(n):
                if sorted_nums[i] != nums[(i + x) % n]:
                    is_sorted = False
                    break

            if is_sorted:
                return True
        
                
        return False