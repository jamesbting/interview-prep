class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False

        self.parent[root_i] = root_j
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u, v):
                return False
        return True