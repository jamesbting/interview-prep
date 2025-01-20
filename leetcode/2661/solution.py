class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        row_count = [0 for _ in range(m)]
        col_count = [0 for _ in range(n)]

        coords = self.buildCoords(mat)
        for x in range(len(arr)):
            i, j = coords[arr[x]]
            
            row_count[i] += 1
            col_count[j] += 1

            if row_count[i] == n:
                return x
            if col_count[j] == m:
                return x
        return x


    def buildCoords(self, mat):
        coords = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                coords[mat[i][j]] = (i, j)
        return coords