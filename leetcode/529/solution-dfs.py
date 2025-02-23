class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click[0], click[1]

        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        self.revealAdjacents(board, (x, y), [[False for _ in range(len(board[0]))] for _ in range(len(board))])
        return board

        
    
    def revealAdjacents(self, board, curr, visited):
        directions = [
            (-1,-1),
            (0,-1),
            (1,-1),
            (-1,0),
            (1,0),
            (-1,1),
            (0,1),
            (1,1)
        ]

        x, y = curr[0], curr[1]
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or visited[x][y]:
            return
        visited[x][y] = True
        if board[x][y] == 'E':
            adj_mines = 0
            for dx, dy in directions:
                if x + dx < 0 or x + dx >= len(board) or y + dy < 0 or y + dy >= len(board[0]):
                    continue

                if board[x + dx][y + dy] == 'M':
                    adj_mines += 1

            if adj_mines > 0:
                board[x][y] = str(adj_mines)
            else:
                board[x][y] = 'B'
                for dx, dy in directions:
                    if x + dx < 0 or x + dx >= len(board) or y + dy < 0 or y + dy >= len(board[0]):
                        continue

                    if board[x + dx][y + dy] == 'E':
                        self.revealAdjacents(board, (x + dx, y + dy), visited)
