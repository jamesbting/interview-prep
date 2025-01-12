class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        ans = [[0] * n for _ in range(m)]
        for i in range(0, len(original)):
            row, col = divmod(i, n)
            ans[row][col] = original[i]
        return ans