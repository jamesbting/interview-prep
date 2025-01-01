class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        #scan the board first to find cells to kill and cells to birth
        cells_to_modify = []

        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0),
            (-1,-1),
            (-1,1),
            (1,-1),
            (1,1),
        ]

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                #count the live neighours
                live_neighbours = 0
                for direction in directions:
                    n_i = i + direction[0]
                    n_j = j + direction[1]
                    if 0 <= n_i and n_i < len(board) and 0 <= n_j and n_j < len(board[0]):
                        live_neighbours += board[n_i][n_j]
                    
                #apply the rules
                if board[i][j] == 1:
                    if live_neighbours < 2 or live_neighbours > 3:
                        cells_to_modify.append((i, j, 0))
                else:
                    if live_neighbours == 3:
                        cells_to_modify.append((i, j, 1))
        
        for cell in cells_to_modify:
            board[cell[0]][cell[1]] = cell[2]