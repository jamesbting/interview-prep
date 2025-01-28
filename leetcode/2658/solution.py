from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
        ]
        visited = [[grid[i][j] == 0 for j in range(n)] for i in range(m)]
        max_fish = 0

        #over all the islands of fish
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    #find the number of fish in this island
                    curr_fish = 0
                    q = deque([(i,j)])
                    while q:
                        
                        x, y = q.popleft()
                        if visited[x][y]:
                            continue
                        curr_fish += grid[x][y]
                        visited[x][y] = True

                        for dx, dy in directions:
                            if 0 <= x + dx < m and 0 <= y + dy < n and not visited[x + dx][y + dy]:
                                q.append((x + dx, y + dy))
                    
                    max_fish = max(max_fish, curr_fish)
        return max_fish
