class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = [
            [-1,0],
            [1,0],
            [0,-1],
            [0,1],
        ]
        m = len(isWater)
        n = len(isWater[0])
        ans = [[-1 for _ in range(n)] for _ in range(m)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i, j, 0))
                    ans[i][j] = 0
        curr_level = 0
        
        while q:
            i, j, distance = q.popleft()
            #get min of all neighbours
            for dx, dy in directions:
                n_i, n_j = i + dx, j + dy
                if 0 <= n_i < m and 0 <= n_j < n:
                    if ans[n_i][n_j] == -1:
                        ans[n_i][n_j] = distance + 1
                        q.append((n_i, n_j, distance + 1))
        return ans
        
            