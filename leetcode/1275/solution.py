class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

        for i in range(0, len(moves)):
            player = "A" if i % 2 == 0 else "B"
            self.play(grid, player, moves[i])
            if self.isWinner(grid, player):
                return player
        
        return "Draw" if len(moves) == 9 else "Pending"

    def play(self, grid, player, move):
        grid[move[0]][move[1]] = player

    def isWinner(self, grid, player):
        for i in range(0, 3):
            if sum([1 if player == grid[i][j] else 0 for j in range(0, 3)]) == 3:
                return True
            if sum([1 if player == grid[j][i] else 0 for j in range(0, 3)]) == 3:
                return True

        if sum([1 if player == grid[j][j] else 0 for j in range(0, 3)]) == 3:
                return True
        if sum([1 if player == grid[2-j][j] else 0 for j in range(0, 3)]) == 3:
                return True
        return False
           
            
        
