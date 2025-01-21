class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        firstRowSum = sum(grid[0])
        secondRowSum = 0
        minimum_sum = math.inf

        for i in range(len(grid[0])):
            firstRowSum -= grid[0][i]
           
            minimum_sum = min(minimum_sum, max(firstRowSum, secondRowSum))
            secondRowSum += grid[1][i]
        return minimum_sum


