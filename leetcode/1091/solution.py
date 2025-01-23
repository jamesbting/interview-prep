from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
            (1,1),
            (1,-1),
            (-1,1),
            (-1,-1)
        ]


        q = deque()
        visited = set()
        if grid[0][0] == 0:
            q.append((0,0,1))
            visited.add((0,0))
        while q:
            q_len = len(q)
            x, y, d = q.popleft()
            if x == n - 1 and y == n - 1:
                return d
            for dx, dy in dirs:
                if 0 <= x + dx < n and 0 <= y + dy < n:
                    if (x + dx, y + dy) not in visited and grid[x + dx][y+dy] == 0:
                        visited.add((x + dx, y + dy))
                        q.append((x + dx, y + dy, d + 1))
        return -1
        

