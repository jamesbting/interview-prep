class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        integer_count = [0 for _ in range(n + 1)]
        ans = []
        commonCount = 0
        for i in range(n):
            integer_count[A[i]] += 1
            if integer_count[A[i]] == 2:
                commonCount += 1

            integer_count[B[i]] += 1
            if integer_count[B[i]] == 2:
                commonCount += 1

            ans.append(commonCount)
        return ans
