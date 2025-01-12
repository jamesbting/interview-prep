class Solution:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        islands = 0

        for i in range(0, self.m):
            for j in range(0, self.n):
                if grid[i][j] == "1":
                    islands += 1
                    self.dfs(grid, i, j)
        return islands

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)
        
