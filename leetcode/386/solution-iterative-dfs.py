class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        curr = 1

        for i in range(n):
            ans.append(curr)
            if curr * 10 <= n:
                curr = curr * 10
            else:
                while curr >= n or curr % 10 == 9:
                    curr = curr // 10
                curr += 1
        return ans
