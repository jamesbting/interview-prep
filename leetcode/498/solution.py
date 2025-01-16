class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        # m - 1 - i
        ans = []
        for d in range(m + n - 1):
            arr = []
            i = 0 if d < n else d - n + 1
            j = d if d < n else n - 1

            while 0 <= i and i < m and 0 <= j and j < n:
                arr.append(mat[i][j])
                i += 1
                j -= 1

            if d % 2 == 0:
                arr.reverse()
            ans.extend(arr)
        
        return ans