class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        d = 1
        ans = []
        i, j = 0, 0
        while i < m and j < n:

            ans.append(mat[i][j])
            newi = i + (-1 if d == 1 else 1)
            newj = j + (1 if d == 1 else - 1)

            if not self.isValid(newi, newj, m, n):
                if d == 1:
                    i += (j == n - 1)
                    j += (j < n - 1)
                else:   
                    j += (i == m - 1)
                    i += (i < m - 1)
                    
                d = 1 - d
            else:
                i = newi
                j = newj

        
        return ans

    def isValid(self, i, j, m, n ):
        return 0 <= i and i < m and 0 <= j and j < n