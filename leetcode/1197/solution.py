class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = [(0,0)]
        dirs = [
            [2,1],
            [2,-1],
            [-2,1],
            [-2,-1],
            [1,2],
            [-1,2],
            [1,-2],
            [-1,-2],
        ]
        steps = 0
        visited = set([(0,0)])
        while q:
            q_len = len(q)
            for i in range(q_len):
                cx, cy = q.pop(0)
                if cx == x and cy == y:
                    return steps

                for dx, dy in dirs:
                    if (cx + dx, cy + dy) not in visited:
                        q.append((cx + dx, cy + dy))
                        visited.add((cx + dx, cy + dy))
            steps += 1
        return steps
