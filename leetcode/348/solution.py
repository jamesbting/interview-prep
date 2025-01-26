class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0 for _ in range(n)]
        self.cols = [0 for _ in range(n)]
        self.diagonal = 0
        self.antidiagonal = 0
    def move(self, row: int, col: int, player: int) -> int:
        self.rows[row] += 1 if player == 1 else -1
        self.cols[col] += 1 if player == 1 else -1        
        #check diagonals

        n = self.n
        if row == col:
            self.diagonal += 1 if player == 1 else -1
        if row == n - 1 - col:
           self.antidiagonal += 1 if player == 1 else -1

       
        if self.rows[row] == n or self.cols[col] == n or self.diagonal == n or self.antidiagonal == n:
            return 1
        
        if self.rows[row] == -n or self.cols[col] == -n or self.diagonal == -n or self.antidiagonal == -n:
            return 2

        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)