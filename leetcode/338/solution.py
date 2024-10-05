class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        

        ans = [0, 1]
        for x in range(2, n + 1):
            if x & (x - 1) == 0:
                ans.append(1)
            else:
                ans.append(ans[x // 2] + (x % 2))
        return ans
