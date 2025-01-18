class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1,0)]
        self.m = len(grid)
        self.n = len(grid[0])
        min_cost = [[math.inf for _ in range(self.n)] for _ in range(self.m)]
        min_cost[0][0] = 0

        pq =[(0,0)]
        
        while len(pq) > 0:
            x, y = pq.pop(0)
            for i, (dx, dy) in enumerate(directions):
                new_x, new_y = x + dx, y + dy
                cost = 0 if grid[x][y] == i + 1 else 1
                if 0 <= new_x < self.m and 0 <= new_y < self.n and min_cost[x][y] + cost < min_cost[new_x][new_y]:
                    min_cost[new_x][new_y] = min_cost[x][y] + cost
                
                    if cost == 1:
                        pq.append((new_x, new_y))
                    else:
                        pq.insert(0,(new_x, new_y))


        return min_cost[self.m-1][self.n-1]
        