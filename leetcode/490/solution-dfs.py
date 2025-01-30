class Solution:
    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        self.m = len(maze)
        self.n = len(maze[0])

        visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        return self.dfs(maze, visited, tuple(start), destination)

        
    def dfs(self, maze, visited, curr, dest):
        x, y = curr
        if visited[x][y]:
            return False
        if x == dest[0] and y == dest[1]:
            return True

        visited[x][y] = True
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
        ]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            while 0 <= new_x < self.m and 0 <= new_y < self.n and maze[new_x][new_y] == 0:
                new_x += dx
                new_y += dy

            if self.dfs(maze, visited, (new_x - dx, new_y - dy), dest):
                return True
        return False
