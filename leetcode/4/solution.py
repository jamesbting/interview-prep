class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        def solve(k, a_start, a_end, b_start, b_end):
            if a_start > a_end:
                return B[k - a_start]
            if b_start > b_end:
                return A[k - b_start]

            a_index, b_index = (a_start + a_end) // 2, (b_start + b_end) // 2
            a_value, b_value = A[a_index], B[b_index]

            if a_index + b_index < k:
                if a_value > b_value:
                    return solve(k, a_start, a_end, b_index + 1, b_end)
                else:
                    return solve(k, a_index + 1, a_end, b_start, b_end)

            else:
                if a_value > b_value:
                    return solve(k, a_start, a_index - 1, b_start, b_end)
                else:
                    return solve(k, a_start, a_end, b_start, b_index - 1)
        len_a, len_b = len(A), len(B)
        n = len_a + len_b
        if (len_a + len_b) % 2 == 1:
            return solve(n // 2 , 0, len_a - 1, 0, len_b - 1)
        else:
            first = solve(n // 2 - 1, 0, len_a - 1, 0, len_b - 1)
            second = solve(n // 2 , 0, len_a - 1, 0, len_b - 1)
            return (first + second) / 2


