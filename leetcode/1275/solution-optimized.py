class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        player = 1
        n = 3
        rows = [0, 0, 0]
        cols = [0, 0, 0]
        antidiag, diag = 0, 0
        for row, col in moves:
            rows[row] += player
            cols[col] += player

            if row == col:
                diag += player
            if col + row == 2:
                antidiag += player

            if any(abs(line) == n for line in [rows[row], cols[col], diag, antidiag]):
                return "A" if player > 0 else "B"
            player *= -1

        return "Draw" if len(moves) == 9 else "Pending"