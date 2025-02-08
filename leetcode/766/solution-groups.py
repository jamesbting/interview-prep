class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        groups = {}
        for i in range(m):
            for j in range(n):
                if i - j not in groups:
                    groups[i - j] = matrix[i][j]
                elif groups[i - j] != matrix[i][j]:
                    return False
        return True
                