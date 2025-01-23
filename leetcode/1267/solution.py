class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rowCount = [sum(grid[i]) for i in range(m)]
        colCount = [sum([grid[i][j] for i in range(m)]) for j in range(n)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rowCount[i] >= 2 or colCount[j] >= 2):
                    ans += 1
        return ans
                