class UnionFind:
    def __init__(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])
        self.parent = []
        self.islands = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.parent.append(i * self.n + j)
                    self.islands += 1
                else:
                    self.parent.append(-1)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i]) 
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            self.parent[rooty] = rootx
            self.islands -= 1
        return 

    def getCount(self):
        return self.islands


class Solution:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        uf = UnionFind(grid)

        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    grid[x][y] == "0"
                    for dx, dy in self.directions:
                        new_x = x + dx
                        new_y = y + dy
                        if 0 <= new_x and new_x < m and 0 <= new_y and new_y < n:
                            if grid[new_x][new_y] == "1":
                                uf.union(x * n + y, new_x * n + new_y)
            
        return uf.getCount()