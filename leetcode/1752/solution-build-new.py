class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        for x in range(n):
            new_arr = [0 for _ in range(n)]
            for i in range(n):
                new_arr[i] = nums[(i + x) % n]

            is_sorted = True
            for i in range(n - 1):
                if new_arr[i] > new_arr[i + 1]:
                    is_sorted = False
                    break

            if is_sorted:
                return True
        
                
        return False