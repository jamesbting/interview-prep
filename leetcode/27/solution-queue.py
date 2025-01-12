class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #find the spot at the end we can remove
        q = []
        for n in nums:
            if n != val:
                q.append(n)
            
        ans = len(q)

        for i in range(len(q)):
            nums[i] = q[i]
        return ans