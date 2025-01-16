class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        #prepend all the Nones to shift the arrays:
        toAdd = m - 1
        for i in range(m):
            mat[i] = [None for _ in range(i)] + mat[i] + [None for _ in range(toAdd - i)]


        ans = []
        for j in range(n + toAdd):
            r = None
            if j % 2 == 1:
                r = range(m)
            else:
                r = range(m - 1, -1, -1)
            for i in r:    
                if mat[i][j] != None:
                    ans.append(mat[i][j])
        return ans


#[
    # [1,2,3,4,N]
    # [N,5,6,7,8]
    # ]

    # [1,2,3,N,N],
    # [N,4,5,6,N],
    # [N,N,7,8,9]
