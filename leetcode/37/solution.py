class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_sets = defaultdict(set)
        col_sets = defaultdict(set)
        square_sets = defaultdict(set)
        n = 9

        # populate all the values
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                square = (i // 3) * 3 + j // 3
                v = int(board[i][j])
                row_sets[i].add(v)
                col_sets[j].add(v)
                square_sets[square].add(v)
        
        def canPlace(i, j, d):
            square = (i // 3) * 3 + j // 3
            return d not in row_sets[i] and d not in col_sets[j] and d not in square_sets[square]

        def backtrack(i, j):
            if i == n - 1 and j == n:
                return True
            elif j == n:
                j = 0
                i += 1


            if board[i][j] != '.':
                return backtrack(i, j + 1)

           
            square = (i // 3) * 3 + j // 3
            for nxt in range(1, n + 1):
                if not canPlace(i, j, nxt):
                    continue
                    
                # place it into the board
                board[i][j] = str(nxt)
                row_sets[i].add(nxt)
                col_sets[j].add(nxt)
                square_sets[square].add(nxt)
                
                
                if backtrack(i, j + 1):
                    return True
                
                #backtrack and remove
                board[i][j] = '.'
                row_sets[i].remove(nxt)
                col_sets[j].remove(nxt)
                square_sets[square].remove(nxt)
                
            return False
        backtrack(0, 0)
               