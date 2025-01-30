from collections import deque
class Solution:
    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])

        visited = [[False for _ in range(n)] for _ in range(m)]
        directions = [
                (0,1),
                (0,-1),
                (1,0),
                (-1,0),
            ]

        q = deque([tuple(start)])
        while q:
            x, y = q.popleft()
            if x == destination[0] and y == destination[1]:
                return True

            visited[x][y] = True
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                while 0 <= new_x < m and 0 <= new_y < n and maze[new_x][new_y] == 0:
                    new_x += dx
                    new_y += dy

                new_x -= dx
                new_y -= dy
                if not visited[new_x][new_y]:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = True
        
        return False


              
