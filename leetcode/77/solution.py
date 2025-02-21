class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(start, curr):
            if len(curr) == k:
                ans.append(curr[:])
                return 
                
            need = k - len(curr)
            available = n - start + 1
            remaining = available - need
            for i in range(start, start + remaining + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()
        backtrack(1, [])
        return ans

    