class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0 for _ in range(len(code))]

        n = len(code)

        decrypted = [0 for _ in range(n)]
        lower, upper = 0, 0
        if k > 0:
            lower, upper = 1, k
        else:
            lower, upper = n + k, n - 1

        window_sum = sum(code[lower:upper + 1])

        for i in range(n):
            decrypted[i] = window_sum

            window_sum -= code[lower % n]
            window_sum += code[(upper + 1) % n]

            lower += 1
            upper += 1
        
        return decrypted
            