class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        a_set = set()
        b_set = set()
        c = []
        for i in range(n):
            a_set.add(A[i])
            b_set.add(B[i])

            c.append(len(a_set.intersection(b_set)))
        return c