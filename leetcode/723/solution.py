class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m = len(board)
        n = len(board[0])
        while True: #until the board is stable
            #flag all the candies to be crushed
            toCrush = [[False for _ in range(n)] for _ in range(m)]
            isStableBoard = True
            # check all the rows
            for i in range(0, m):
                for j in range(0, n):
                    if board[i][j] != 0:
                        if  i < m - 2 and board[i][j] == board[i + 1][j] and board[i + 1][j] == board[i + 2][j]:
                            toCrush[i][j] = True
                            toCrush[i+1][j] = True
                            toCrush[i+2][j] = True
                            isStableBoard = False

                        if  j < n - 2 and board[i][j] == board[i][j + 1] and board[i][j+1] == board[i][j+2]:
                            toCrush[i][j] = True
                            toCrush[i][j+1] = True
                            toCrush[i][j+2] = True
                            isStableBoard = False
                    
            if isStableBoard:
                return board
            
            #gravity step
            # for each column count number of trues below each cell, and move each cell down by that much
            for j in range(0, n):
                #count trues and build new column to copy
                totalTrues = 0
                truesBelowEach = [0] * m
                col = []
                for i in range(m - 1, -1, -1):
                    truesBelowEach[i] = totalTrues
                    totalTrues = totalTrues + 1 if toCrush[i][j] else totalTrues

                    if not toCrush[i][j]:
                        col.append(board[i][j])
                    
                col.reverse()
                col = [0] * totalTrues + col

                for i, el in enumerate(col):
                    board[i][j] = col[i]
            