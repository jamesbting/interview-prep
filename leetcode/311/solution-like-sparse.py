class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        
        for j in range(n):
            col = [mat2[u][j] for u in range(k)]
            for i in range(m):
                ans[i][j] = self.dot_product(mat1[i], col)
                
        return ans



    def dot_product(self, v1, v2):
        v1_map = [(i, n) for i, n in enumerate(v1) if n != 0]
        v2_map = [(i, n) for i, n in enumerate(v2) if n != 0]

        ans = 0
        i, j = 0, 0
        while i < len(v1_map) and j < len(v2_map):
            if v1_map[i][0] == v2_map[j][0]:
                ans += v1_map[i][1] * v2_map[j][1]
            if v1_map[i][0] < v2_map[j][0]:
                i += 1
            else:
                j += 1
        return ans