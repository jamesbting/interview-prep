class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
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

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        q = deque()
        q.append(click)
        while q:
            curr = q.pop()
            x, y = curr[0], curr[1]
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or visited[x][y] or board[x][y] != 'E':
                continue

            mines = 0
            for dx, dy in directions:
                if x + dx < 0 or x + dx >= len(board) or y + dy < 0 or y + dy >= len(board[0]):
                    continue
                
                if board[x + dx][y + dy] == 'M':
                    mines += 1
                
            if mines > 0:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for dx, dy in directions:
                    if x + dx < 0 or x + dx >= len(board) or y + dy < 0 or y + dy >= len(board[0]):
                        continue
                    q.append((x + dx, y + dy))

        return board                

    
      