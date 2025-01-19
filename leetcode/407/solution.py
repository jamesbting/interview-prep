class Solution:
    class Cell:
        def __init__(self, height, r, c):
            self.height = height
            self.r = r
            self.c = c

        def __lt__(self, other):
            return self.height < other.height

    def isvalid(self, r, c):
        return 0 <= r < self.m and 0 <= c < self.n

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        self.m = len(heightMap)
        self.n = len(heightMap[0])
        d_row = [0,0,-1,1]
        d_col = [-1,1,0,0]

        visited  = [[False for _ in range(self.n)] for _ in range(self.m)]

        heap = []
        for i in range(self.m):
            heapq.heappush(heap, self.Cell(heightMap[i][0], i, 0))
            heapq.heappush(heap, self.Cell(heightMap[i][self.n - 1], i, self.n - 1))
            visited[i][0] = visited[i][self.n - 1] = True


        for j in range(self.n):
            heapq.heappush(heap, self.Cell(heightMap[0][j], 0, j))
            heapq.heappush(heap, self.Cell(heightMap[self.m - 1][j], self.m - 1, j))
            visited[0][j] = visited[self.m - 1][j] = True

        total_volume = 0
        while len(heap) > 0:
            cell = heapq.heappop(heap)

            r = cell.r
            c = cell.c
            min_height = cell.height

            for direction in range(4):
                new_r = r + d_row[direction]
                new_c = c + d_col[direction]

                if self.isvalid(new_r, new_c) and not visited[new_r][new_c]:
                    neighbour_height = heightMap[new_r][new_c]

                    if neighbour_height < min_height :
                        total_volume += min_height - neighbour_height
                    heapq.heappush(heap, self.Cell(
                        max(neighbour_height, min_height),
                        new_r,
                        new_c
                    ))
                    visited[new_r][new_c] = True
        return total_volume  
