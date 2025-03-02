class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m1, m2, n1, n2 = len(mat1), len(mat2), len(mat1[0]), len(mat2[0])
        ans = [[0 for _ in range(n2)] for _ in range(m1)]
        m1_vals, m2_vals = defaultdict(dict), defaultdict(dict)
        for i in range(m1):
            for j in range(n1):
                if mat1[i][j] != 0:
                    m1_vals[j][i] = mat1[i][j]
        print(m1_vals)
        for i in range(m2):
            for j in range(n2):
                if mat2[i][j] != 0:
                    m2_vals[i][j] = mat2[i][j]
        print(m2_vals)
        for j in m1_vals:
            for i in m1_vals[j]:
                for k in m2_vals[j]:
                    ans[i][k] += m1_vals[j][i] * m2_vals[j][k]
        return ans
