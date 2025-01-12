class Solution:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == "1":
                    islands += 1
                    self.bfs(grid, i, j)
        return islands

    def bfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        q = []
        q.append((i, j))
        
        while len(q) > 0:
            x, y = q.pop(0)
            for dx, dy in self.directions:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x and new_x < m and 0 <= new_y and new_y < n:
                    if grid[new_x][new_y] == '1':
                        grid[new_x][new_y] = '0'
                        q.append((new_x, new_y))
        
