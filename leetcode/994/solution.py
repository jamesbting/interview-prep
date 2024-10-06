class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []

        fresh = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 2:
                    queue.append((i, j, 0))
                if col == 1:
                    fresh += 1

        max_mins = 0

        while len(queue) > 0:
            curr = queue.pop(0)
            i, j, mins = curr
            max_mins = max(mins, max_mins)

            if i > 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                fresh -= 1
                queue.append((i - 1, j, mins + 1))
            if i < len(grid) - 1 and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                fresh -= 1
                queue.append((i + 1, j, mins + 1))
            if j > 0 and grid[i][j - 1] == 1:
                grid[i][j-1] = 2
                fresh -= 1
                queue.append((i, j - 1, mins + 1))
            if j < len(grid[i]) - 1 and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                fresh -= 1
                queue.append((i, j + 1, mins + 1))
            

        if fresh > 0:
            return -1

        return max_mins